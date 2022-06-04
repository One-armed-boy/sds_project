from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from res.models import Review
from res.serializers import ReviewSerializer
from rest_framework.response import Response
# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class my_review(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        reviews=Review.objects.filter(author=request.user)
        if reviews:
            serializer=ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        else:
            return Response('없다.')