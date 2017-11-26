from django.conf.urls import url
from cm_goods import views

urlpatterns = [
	url(r'^$',views.index,name='index'), # 首页
	url(r'^new/$',views.new,name="new_recommend"), # 新品推荐
]