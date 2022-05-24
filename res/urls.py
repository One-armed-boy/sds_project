from django.urls import path,include
from . import views

app_name='res'

urlpatterns=[
    path('<int:res_id>/',views.res_detail.as_view(),name='res_detail'),
    path('<int:is_pred>/<int:author_id>/',views.ResListUp.as_view(),name='res_listup'),
    #path('visited/<int:author_id>/',views.visited_res.as_view(),name='visited_res'),
]