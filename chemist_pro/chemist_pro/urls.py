"""chemist_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^tinymce/', include('tinymce.urls')),# 富文本编辑器
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/',include('cm_user.urls',namespace="user")),
    url(r'^',include('cm_goods.urls',namespace='goods')),
    url(r'^cart/',include('cm_cart.urls',namespace='cart')),
    url(r'^order/',include('cm_order.urls',namespace='order')),
    url(r'^shop/',include('cm_shop.urls',namespace='shop')),
]
