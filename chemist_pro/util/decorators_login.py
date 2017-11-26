from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse


def login_require(func_view):
	def midd_ware(request,*args,**kwargs):
		if request.session.has_key('islogin'):
			return func_view(request,*args,**kwargs)
		else:
			return redirect(reverse('user:login'))
	return midd_ware