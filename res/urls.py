from django.urls import path,include
from . import views

app_name='res'

urlpatterns=[
    path('<int:res_id>/',views.res_detail.as_view(),name='res_detail'),
    path('visited/',views.Visited.as_view(),name='visited'),
    path('recommendation/',views.Recommendation.as_view(),name='recommendation'),
    path('scoring/<int:res_id>/',views.scoring.as_view(), name='scoring')
    #path('visited/<int:author_id>/',views.visited_res.as_view(),name='visited_res'),
]