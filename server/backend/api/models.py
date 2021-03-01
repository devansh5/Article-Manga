from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class CustomUser(AbstractUser):
    fullname=models.CharField(max_length=100,blank=True)



    def __str__(self):
        return self.fullname

class Articles(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100,blank=True,default='')
    body=models.TextField(blank=True,default='')
    image_url=models.CharField(max_length=300)
    owner=models.ForeignKey(CustomUser,related_name='articles',on_delete=models.CASCADE)


    class Meta:
        ordering=['created']

# @receiver(post_save,sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender,instance=None,created=False,**kwargs):
#     if created:
#         Token.objects.create(user=instance)