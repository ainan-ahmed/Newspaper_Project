from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['username','first_name','last_name','email','date_of_birth'] #controls the fields to be listed in django admin
    
admin.site.register(CustomUser,CustomUserAdmin)