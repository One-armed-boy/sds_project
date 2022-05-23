from rest_framework import serializers
from .models import Res,Review

class ResSerializer(serializers.ModelSerializer):
    class Meta:
        model=Res
        fields=['name','address','phone']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['author','res','score','comment','create_date']