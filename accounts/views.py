from rest_framework import status
from rest_framework.generics import CreateAPIView,GenericAPIView
from rest_framework.response import Response
from .serializers import SignupSerializer, LoginSerializer
from .models import AppUser
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate, login, logout
# Create your views here.

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


class Login(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.initial_data['email']
            password = serializer.initial_data['password']
            user = authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        logout(request)
        return Response('LogOut Successful!')
