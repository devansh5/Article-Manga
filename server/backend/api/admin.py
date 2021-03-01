from django.contrib import admin
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    models=CustomUser

admin.site.register(CustomUser,CustomUserAdmin)



