from django.contrib import admin
from .models import *
# Register your models here.

class InPicAdmin(admin.ModelAdmin):
    list_display = ['guidmodel_ptr_id', 'before', 'created']

class OutPicAdmin(admin.ModelAdmin):
    list_display = ['guidmodel_ptr_id', 'after', 'created']


admin.site.register(OutPic, OutPicAdmin)
admin.site.register(InPic, InPicAdmin)
