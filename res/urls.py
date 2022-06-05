from django.urls import path,include
from . import views

app_name='res'

urlpatterns=[
    path('',views.index.as_view(),name='index'),
    path('search/kw=<str:kw>/',views.res_search.as_view(),name='search'),
    path('all/',views.All.as_view(),name='all'),
    path('<int:res_id>/',views.res_detail.as_view(),name='res_detail'),
    path('<int:res_id>/review/',views.review_list.as_view(),name='reviews'),
    path('visited/',views.Visited.as_view(),name='visited'),
    path('recommendation/',views.Recommendation.as_view(),name='recommendation'),
    path('scoring/create/',views.scoring_create.as_view(), name='scoring_create'),
    path('scoring/update/',views.scoring_update.as_view(), name='scoring_update'),
    path('scoring/delete/<int:res_id>',views.scoring_delete.as_view(), name="scoring_delete"),
    path('add/',views.add_res_reserve.as_view(),name='add'),
    #path('visited/<int:author_id>/',views.visited_res.as_view(),name='visited_res'),
]