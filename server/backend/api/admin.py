from django.contrib import admin
from .models import CustomUser,Articles
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    models=CustomUser

admin.site.register(CustomUser,CustomUserAdmin)


admin.site.register(Articles)



