from django.conf.urls import url
from cm_user import views

urlpatterns = [
	url(r'^register/$',views.register,name='register'), # 用户注册处理
	url(r'^register_check/$',views.register_check), # 注册验证

	url(r'^login/$',views.login,name="login"), # 用户登陆
	url(r'^login_check/$',views.login_check,name='check_login'), # 登陆验证

	
	url(r'^personal/$',views.personal,name='personal'), # 登陆验证
]