from django.urls import include,path
from rest_framework.authtoken import views
from .views import UserListView,UserCreateAPIView,UserLoginAPIView,ArticleList

urlpatterns=[
    path('',UserListView.as_view()),
    path('signup/',UserCreateAPIView.as_view(),name='user-register'),
    path('login/',UserLoginAPIView.as_view(),name='user-login'),
    path('articles/',ArticleList.as_view(),name='article-detail')

    # path('articles/',ArticleListAPIView.as_view(),name='article-list'),
    # path('write/<int:pk>/',ArticleCreateAPIView.as_view(),name='article-create'),
    # path('articles/user/<int:pk>',ArticleDetailAPIView.as_view(),name='article-detail')
]