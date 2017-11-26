from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse
import re
from cm_user.models import Passport
# from util.get_hashlib import put_bcrypt
from util.get_hashlib import get_hash
from util.decorators_login import login_require




# user/register/
def register(request):
    '''显示注册页面'''
    return render(request,'cm_user/register.html')

# user/register_check/
def register_check(request):
    '''注册信息校验'''
    # 0.接收用户注册信息
    tel = request.POST.get('tel')
    pwd = request.POST.get('pwd')
    check_code = request.POST.get('check_code')

    # 1.验证注册信息为空
    if not all([tel,pwd,check_code]):
        return render(request,'cm_user/register.html',{'errmsg':'注册参数不能为空'})
    # 2.验证电话号码
    if not re.match(r'^((13[0-9])|(14[7])|(15([0-3]|[5-9]))|(17[6-8])|(18[0-3,5-9]))\d{8}$',tel):
        return render(request,'cm_user/register.html',{'errmsg':'电话号码不合法!'})
    # 3.校验验证码

    # 4.添加数据库
    passport = Passport.objects.add_one_passport(tel = tel,password =pwd)
    return redirect(reverse('user:login'))

# /user/login/
def login(request):
    '''显示登陆页面'''
    return render(request,'cm_user/login.html')


# /user/login_check
def login_check(request):
    '''登陆验证'''
    passport = request.POST.get('username')
    password = request.POST.get('password')

    # print(passport)
    # print(password)
    if not all([passport,password]):
         return JsonResponse({'res':0,'errmsg':'登陆参数不能为空'})
    try:
        # 1.按照电话号码进行登陆
        username = Passport.objects.get(tel = passport,password = get_hash(password))
        # 2.按照邮箱登陆
        # 3.按照用户名登陆
        
        # 如果查询到信息
        if username:
            # 1.记录登陆状态
            print(request.session.get('url_path'))
            next_url = request.session.get('url_path', reverse('goods:index'))
            r_ajax = JsonResponse({"res":1,'next_url':next_url})
            
            r_ajax.set_cookie('username',username,max_age = 2*7*24*3600)
            # 保存登录状态
            request.session['islogin'] = True
            request.session['username'] = username.username
            request.session['username_id'] = username.id

            print(request.session.get('username'))
            print(request.session.get('username_id'))
            print(request.session.get('islogin'))
            return r_ajax
    except:
        return JsonResponse({'res':0,'errmsg':'用户名或密码错误'})
    

# user/personal/
@login_require
def personal(request):
    '''个人中心'''
    username = request.session.get('username')
    passport = Passport.objects.get(username=username)

    return render(request,'cm_user/personalCenter.html',{"passport":passport})



