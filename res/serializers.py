from rest_framework import serializers
from .models import Res,Review,reserve

class ResSerializer(serializers.ModelSerializer):
    class Meta:
        model=Res
        fields=['id','name','address','phone']
    name = serializers.CharField(max_length=30, required=False, allow_blank=False)
    address = serializers.CharField(max_length=50, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model=reserve
        fields=['id','name','address','phone']
    name = serializers.CharField(max_length=30, required=False, allow_blank=False)
    address = serializers.CharField(max_length=50, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['author','res','score','comment','create_date']
    create_date = serializers.DateTimeField(required=False)
