from rest_framework import serializers


from . import models


class UserSerializer(serializers.ModelSerializer):
    articles=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model=models.CustomUser
        fields=('fullname','username','articles') 



class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.CustomUser
        fields=('fullname','username','password')
        extra_kwargs={'password':{'write_only':True,'min_length':8}}

    

    def create(self,validated_data):
        user=super(UserCreateSerializer,self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class ArticleSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=models.Articles
        fields=('id','title','body','image_url','owner')



