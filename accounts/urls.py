from django.urls import path,include
from .views import SignUp,Login,Logout


app_name='accounts'

urlpatterns=[
    #로그인/회원가입
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('signup/',SignUp.as_view(),name='signup'),
]