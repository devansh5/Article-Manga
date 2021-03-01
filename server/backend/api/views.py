from rest_framework import generics,status
from django.contrib.auth import authenticate
from . import models
from .models import CustomUser,Articles
from rest_framework.views import APIView
from . import serializers
from .serializers import UserSerializer,UserCreateSerializer,ArticleSerializer
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
# Create your views here.

class UserListView(generics.ListAPIView):
    queryset=models.CustomUser.objects.all()
    serializer_class=serializers.UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class=serializers.UserCreateSerializer
    def post(self,request,format='json'):
        serializer=UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token,created=Token.objects.get_or_create(user=user)
            json=serializer.data
            json['token']=token.key
            if user:
                return Response(json,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    permission_classes=()
    def get(self, request,*args,**kwargs):
        token_key = request.headers['Authorization']
        user=Token.objects.get(key=token_key).user
        username=user.username
        if username:
            return Response({"success":"success","username":username},status=status.HTTP_200_OK)

        return Response({"error":"Not authorized user"},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        token=Token.objects.get(user=user).key
        if user:
            return Response({"token":token,"success":"success","fullname":user.fullname,"username":user.username},status=status.HTTP_200_OK)
        return Response({"error":"Wrong Credential"},status=status.HTTP_400_BAD_REQUEST)



class ArticleList(generics.ListCreateAPIView):
    queryset=Articles.objects.all()
    serializer_class=serializers.ArticleSerializer


    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)