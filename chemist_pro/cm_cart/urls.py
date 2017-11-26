from django.conf.urls import url
from cm_cart import views

urlpatterns = [
	url(r'^$',views.cart,name='cart'), # 购物车
	url(r'^add_cart/$',views.add_cart,name='add_cart'), # 添加购物车
	url(r'^update/$',views.update,name='update'), # 更改购物车数量
	]