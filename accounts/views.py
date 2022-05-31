from rest_framework import status
from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework.response import Response
from .serializers import SignupSerializer, LoginSerializer
from .models import AppUser
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
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
'''
class SignUp(CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            AppUser.objects.create_user(
                serializer.initial_data['email'],
                serializer.initial_data['password'],
            )

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
'''
'''
class Login(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.initial_data['email']
            password = serializer.initial_data['password']
            #user = authenticate(request,username=email,password=password)
            user = AppUser.objects.filter(email=email).first()
            if user is None:
                return Response('존재하지 않는 이메일입니다.', status=status.HTTP_400_BAD_REQUEST)
            if not check_password(password,user.password):
                return Response('잘못된 비밀번호 입니다.', status=status.HTTP_400_BAD_REQUEST)
            if user is not None:
                token=TokenObtainPairSerializer.get_token(user)
                refresh_token = str(token)
                access_token = str(token.access_token)
                login(request,user)
                response= Response({"user":serializer.data,
                                 'messages':'login_success',
                                 'jwt_token':{'access_token':access_token,
                                              'refresh_token':refresh_token}},
                                status=status.HTTP_200_OK)
                response.set_cookie('access_token', access_token, httponly=True)
                response.set_cookie('refresh_token', refresh_token, httponly=True)
                return response

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
'''
class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        logout(request)
        return Response('LogOut Successful!')
'''