from django.urls import path,include
from . import views

app_name='res'

urlpatterns=[
    path('<int:res_id>/',views.res_detail,name='res_detail'),
    path('unvisited/<int:author_id>/',views.unvisited_res,name='unvisited_res'),
    path('visited/<int:author_id>/',views.visited_res,name='visited_res'),
]