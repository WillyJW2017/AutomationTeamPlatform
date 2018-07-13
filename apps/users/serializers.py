from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','password',)


class UserFullInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserUpdateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'name', 'avatar', 'currentProject')
