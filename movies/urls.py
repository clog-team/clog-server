from django.urls import path
from .views import *

urlpatterns = [
  path('<str:movie_name>/', search, name="search"),
]