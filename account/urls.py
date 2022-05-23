from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns=[
    path('signup/',views.signup_view, name='signup_view'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view, name='logout_view'),
]