from django.contrib import admin
from cm_goods.models import * 


class GoodstAdmin(admin.ModelAdmin):
    list_display = ['id','name','desc','shop_name','type_id','sales']

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','name','addr','detail']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','name','image']


admin.site.register(Type,TypeAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(Goods,GoodstAdmin)
