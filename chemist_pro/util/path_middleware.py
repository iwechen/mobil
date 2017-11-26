

class UrlPathRecordMiddleWare(object):
	'''记录登陆跳转中间件'''
	# 记录不用记录的路径
	EXCLUDE_URLS = ['/user/login/','/user/register/']

	
	def process_view(self,request,view_func,*view_args,**view_kwargs):
		if request.path not in UrlPathRecordMiddleWare.EXCLUDE_URLS and not request.is_ajax() and request.method=='GET':
			request.session['url_path'] = request.path




class UrlPathRecordMiddleWareCart(object):
	'''记录购物车返回中间件'''
	# 记录不用记录的路径
	EXCLUDE_URLS = ['/user/login/','/user/register/','/cart/']

	def process_view(self,request,view_func,*view_args,**view_kwargs):
		if request.path not in UrlPathRecordMiddleWareCart.EXCLUDE_URLS and not request.is_ajax() and request.method=='GET':
			request.session['url_path_cart'] = request.path
