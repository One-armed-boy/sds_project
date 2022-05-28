from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import AppUser

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=AppUser.objects.all())]
    )

    class Meta:
        model = AppUser
        fields = ('email',  'password')

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'})
    email = serializers.EmailField(required=True, allow_blank=False)
    class Meta:
        model = AppUser
        fields = ('email','password')
