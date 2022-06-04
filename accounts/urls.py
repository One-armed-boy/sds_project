from django.urls import path,include
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import my_review
app_name='accounts'

urlpatterns=[
    #로그인/회원가입
    #path('login/',Login.as_view(),name='login'),
    #path('logout/',Logout.as_view(),name='logout'),
    #path('signup/',SignUp.as_view(),name='signup'),
    path('token/verify',TokenVerifyView.as_view(), name='token_verify'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('mypage/myreview/',my_review.as_view(),name="my_review"),
]