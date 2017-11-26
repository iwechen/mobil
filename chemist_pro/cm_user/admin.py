from django.contrib import admin
from cm_user.models import * 


class PassportAdmin(admin.ModelAdmin):
	list_display = ['id','username','tel','email','is_shop']


admin.site.register(Passport,PassportAdmin)
