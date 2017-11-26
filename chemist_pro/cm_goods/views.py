from django.shortcuts import render,redirect
from cm_goods.models import Type,Shop,Goods




# /
def index(request):
    '''首页'''
    type_goods = Type.objects.all()

    return render(request,'cm_goods/index.html',{'type_goods':type_goods})

# /new/
def new(request):
    '''新品推荐'''
    goods = Goods.objects.all()
    return render(request,'cm_goods/new_recommend.html',{'goods':goods})


