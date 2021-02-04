# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.serializers import *
import urllib.request as ul
import os, json, ssl
from urllib.parse import quote
from pathlib import Path

# 영화진흥위원회 api key
def get_api_key(type):
  BASE_DIR = Path(__file__).resolve().parent.parent
  CREDENTIAL_FILE = os.path.join(BASE_DIR, 'credentials.json')
  credentials = json.loads(open(CREDENTIAL_FILE).read())

  if type is 'image':
    return credentials["NAVER_CLIENT_ID"], credentials["NAVER_CLIENT_SECRET"]
  elif type is 'detail':
    return credentials["MOVIE_DETAIL_API_KEY"]
  else:
    return credentials["MOVIE_API_KEY"]


# 영화 이미지
@api_view(['GET'])
def image(request, movie_name):
  client_id, client_secret = get_api_key("image")
  query = quote(movie_name)

  url = "https://openapi.naver.com/v1/search/movie.json?query={}".format(query)
  request = ul.Request(url)
  request.add_header("X-Naver-Client-Id", client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  context = ssl._create_unverified_context()

  response = ul.urlopen(request, context=context)
  rescode = response.getcode()

  if (rescode == 200):
    response_data = json.loads(response.read())
    return Response(data=response_data)
  else:
    print("Error code: " + rescode)


# 영화목록
@api_view(['GET'])
def search(request, movie_name):
  key = get_api_key("list")
  query = quote(movie_name)

  url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={}&movieNm={}".format(key, query)
  request = ul.Request(url)

  response = ul.urlopen(request)
  rescode = response.getcode()

  if (rescode == 200):
    response_data = json.loads(response.read())
    return Response(data=response_data)
  else:
    print("Error code: " + rescode)


# 영화 상세정보
@api_view(['GET'])
def detail(request, movie_cd):
  key = get_api_key("detail")
  
  url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={}&movieCd={}".format(key, movie_cd)

  request = ul.Request(url)

  response = ul.urlopen(request)
  rescode = response.getcode()

  if (rescode == 200):
    response_data = json.loads(response.read())
    return Response(data=response_data)
  else:
    print("Error code: " + rescode)
