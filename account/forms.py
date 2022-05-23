from rest_framework import serializers
from .models import User

class PostUserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['username','password1','password2','nickname','phone']

   def create(self,validated_data):
      user = User.objects.create_user(validated_data['username'], None, validated_data['password'])
      return user