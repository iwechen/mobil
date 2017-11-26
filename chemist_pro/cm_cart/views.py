from django.shortcuts import render
from django.core.urlresolvers import reverse
from util.decorators_login import login_require
from django_redis import get_redis_connection
from django.http import HttpResponse,JsonResponse
from cm_goods.models import Goods,Shop
import json
import re


@login_require
def cart(request):
    '''购物车'''
    # 通过id查询购物车
    con = get_redis_connection('default')
    cart_key = 'cart_%d'%(request.session.get('username_id'))
    # {goods_id:goods_count,goods_id:goods_count}
    cart_dict = con.hgetall(cart_key)
    print(cart_dict)
    goods_sum = 0
    type_li = []
    for type_id, goods_str in cart_dict.items():
        type_id = type_id.decode('utf-8')
        goods_str = goods_str.decode('utf-8')
        # 获取店铺id和商品id字符串
        type_id = str(json.loads(type_id))
        goods_str = str(json.loads(goods_str))
        # print(goods_str)
        types = Shop.objects.get(id=type_id)
        # print(types.name)
        # print(len(goods_str))
        # 商品总数
        goods_sum += len(goods_str)
        # 将商品放入集合去重
        goods_set= set()
        for goods_id in goods_str:
            # print(goods_id)
            goods_set.add(goods_id)
        # 返回商品id,不重复
        # print(goods_set)
        goods_li=[]
        # 遍历查询商品
        for goods_id in goods_set:
            # print(goods_id)
            goods = Goods.objects.get_goods_by_id(goods_id=goods_id)
            # 给商品添加数量属性
            goods.count = goods_str.count(goods_id)
            goods_li.append(goods)
        types.goods_li = goods_li

        type_li.append(types)
        # print(types.id)

    # 返回跳转地址
    next_url = request.session.get('url_path_cart', reverse('goods:index'))

    contex = {'next_url':next_url,'goods_sum':goods_sum,'type_li':type_li}
    return render(request,'cm_cart/cart.html',contex)



def add_cart(request):
    '''添加购物车'''
    # 1,判断用户登录
    if not request.session.has_key('islogin'):
        return  JsonResponse({'ret':0,'errmsg':'您还没有登录，请登录'})
    # 接收提交购物车信息
    goods_id = request.POST.get('goods_id')
    # print(type(goods_id))
    goods = Goods.objects.get_goods_by_id(goods_id=goods_id)
    type_id = goods.shop_name_id
    # print("店铺id:------------>>>",type_id)
    # 3,添加django-redis数据库
    con = get_redis_connection('default')
    cart_key = 'cart_%d'%(request.session.get('username_id'))
    # 查询数据库中是否有此商品
    res = con.hget(cart_key, type_id)
    # print("查询购物车商品id:------------>>>",res)
    try:
        res = res.decode('utf-8')
        res = str(json.loads(res)) 
        # print(type(res))
    except:
        pass
    # print('-------------')
    if res is None:
        # 购物车没添加此商品
        res = goods_id
        # print("no",res)
    else:
        # 购物车已近有此商品，数量相加
        res += goods_id
        # print("已经有",res)
    # 添加到购物车
    con.hset(cart_key,type_id,res)
    return JsonResponse({'ret':5})


# /cart/update/
def update(request):
    '''更新购物车数量'''
    # 0.判断登陆
    if not request.session.has_key('islogin'):
        return JsonResponse({'res':2,'errmsg':'未登录'})
    # 1.接收数据：商品id，加减操作，店铺id
    goods_id = request.POST.get('gc_id')
    m = request.POST.get('m')
    shop_id = request.POST.get('sp_id')
    # 2.校验数据完整
    if not all([goods_id,m,shop_id]):
        return JsonResponse({'res':0,'arrmsg':'添加失败'})
    # 3.获取购物车数据
    con = get_redis_connection('default')
    cart_key = 'cart_%d'%(request.session.get('username_id'))
    # {goods_id:goods_count,goods_id:goods_count}
    goods_id_str = con.hmget(cart_key,shop_id)[0]
    goods_id_str = goods_id_str.decode('utf-8')
    goods_id_str = str(json.loads(goods_id_str))
    print('原字符串')
    print(type(goods_id_str),goods_id_str)
    print('长度')
    print(goods_id_str.count(goods_id))
    # 4.1加操作
    if m == '1':
        goods_id_str += goods_id 
        con.hset(cart_key,shop_id,goods_id_str)
        return JsonResponse({'res':1})
    # 4.2减操作
    elif (goods_id_str.count(goods_id)>1)and m == '0':
        # print('减操作')
        # print(type(goods_id),goods_id)
        goods_id_str = re.sub(goods_id,'',goods_id_str,count=1)
        # print('减后')
        # print(goods_id_str)

        # con = get_redis_connection('default')
        con.hset(cart_key,shop_id,goods_id_str)
        # --------------xxx--------------------
        cart_dict = con.hgetall(cart_key)
        # print('结果')
        # print(cart_dict)
        # ----------------xxx--------------------
        return JsonResponse({'res':1})
    # 4.3未知请求
    else:
        return JsonResponse({'res':3,'errmsg':'操作失败'})





    
