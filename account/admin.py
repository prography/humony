from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import UserCreationForm, UserChangeForm
# from .models import GusetEmail
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
# from customauth.models import User
from .models import User

# User = get_user_model()
#
# class UserAdmin(BaseUserAdmin):
#     search_fields = ('email',)
#     form = UserChangeForm #update view
#     add_form = UserCreationForm #create view
#     model = User
#     list_display = ('email', 'is_admin')
#  #   class Meta:
#   #      model = User
#
# admin.site.register(User, UserAdmin )

#class GuestEimailAdmin(admin.ModelAdmin):
#    search_fields = ['email']
#    class Meta:
#        model = GuestEimail

# admin.site.register(GusetEmail, GuestEmailAdmin )