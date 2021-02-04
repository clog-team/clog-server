from django.urls import path
from .views import *

urlpatterns = [
  path('<str:movie_name>/', search, name="search"),
  path('detail/<int:movie_cd>/', detail, name="detail"),
  path('image/<str:movie_name>/', image, name="image"),
]