from django.urls import path,include
from . import views

app_name='res'

urlpatterns=[
    path('<int:res_id>/',views.res_detail.as_view(),name='res_detail'),
    path('<int:res_id>/review/',views.review_list.as_view(),name='reviews'),
    path('visited/',views.Visited.as_view(),name='visited'),
    path('recommendation/',views.Recommendation.as_view(),name='recommendation'),
    path('scoring/create/',views.scoring_create.as_view(), name='scoring_create'),
    path('scoring/update/',views.scoring_update.as_view(), name='scoring_update'),
    path('add/',views.add_res_reserve.as_view(),name='add'),
    #path('visited/<int:author_id>/',views.visited_res.as_view(),name='visited_res'),
]