# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.serializers import *
import urllib.request as ul
import os, json
from urllib.parse import quote
from pathlib import Path

# 영화진흥위원회 api key
def get_api_key(type):
  BASE_DIR = Path(__file__).resolve().parent.parent
  CREDENTIAL_FILE = os.path.join(BASE_DIR, 'credentials.json')
  credentials = json.loads(open(CREDENTIAL_FILE).read())

  if type is 'detail':
    key = credentials["MOVIE_DETAIL_API_KEY"]
  else:
    key = credentials["MOVIE_API_KEY"]
  return key

# 영화목록
@api_view(['GET'])
def search(request, movie_name):
  key = get_api_key("list")
  query = quote(movie_name)

  url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={}&movieNm={}".format(key, query)
  request = ul.Request(url)

  response = ul.urlopen(request)
  rescode = response.getcode()

  if(rescode == 200):
    response_data = json.loads(response.read())
    return Response(data=response_data)

# 영화 상세정보
@api_view(['GET'])
def detail(request, movie_cd):
  key = get_api_key("detail")
  
  url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}".format(key, movie_cd)

  request = ul.Request(url)

  response = ul.urlopen(request)
  rescode = response.getcode()

  if(rescode == 200):
    response_data = json.loads(response.read())
    return Response(data=response_data)
