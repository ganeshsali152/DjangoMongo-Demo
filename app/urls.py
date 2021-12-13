from app.views import *
from django.urls import path

urlpatterns = [
    path('movies', MovieViewSet.as_view(), name='movies' ),
    path('create/movie', MovieCreateAPIView.as_view(), name='create_movie' ),
    path('movie/<str:title>', MovieByTitleAPIView.as_view(),name='get_single_movie'),
    path('movie/edit/<str:title>', MovieUpdateAPIView.as_view(),name='get_single_movie'),
    path('movie/delete/<str:title>', MovieDeleteAPIView.as_view(),name='delete_movie'),

]
