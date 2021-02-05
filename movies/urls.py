from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
  path('search/<str:movie_name>/', search, name="search"),
  path('detail/<int:movie_cd>/', detail, name="detail"),
  path('naver_api/<str:movie_name>/', naver_api, name="naver_api"),
  path('old/', old, name="old"),
  path('recent/', recent, name="recent"),
  path('recommend/', recommend, name="recommend"),
  # path('pending/', prediction, name="prediction"),
  url(r'^pending/$', prediction),
  url(r'^record/$', record),
]