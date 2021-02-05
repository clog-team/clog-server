from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
  path('search/<str:movie_name>/', search, name="search"),
  path('detail/<int:movie_cd>/', detail, name="detail"),
  path('image/<str:movie_name>/', image, name="image"),
  path('old/', old, name="old"),
  path('recent/', recent, name="recent"),
  # path('pending/', prediction, name="prediction"),
  url(r'^pending/$', prediction),
]