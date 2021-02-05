from django.contrib.auth.models import User
from django.db import models

# 영화
class Movie(models.Model):
  movie_code = models.CharField(max_length=20) # 영화진흥위원회 영화코드
  title = models.CharField(max_length=500) # 영화제목
  opening_date = models.CharField(max_length=20) # 개봉일
  directors = models.TextField() # 감독
  thumbnail_url = models.TextField() # 사진
  genre = models.CharField(max_length=200) # 장르
  running_time = models.IntegerField() # 상영시간
  average_rating = models.DecimalField(max_digits=6, decimal_places=2) # 전체 평점 평균
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


# 기록
class Record(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # 영화
  rating = models.IntegerField() # 평점
  comment = models.TextField() # 코멘트(한줄평)
  recommend = models.IntegerField() # 추천여부(0: 추천하지 않음, 1: 추천함)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


# 위시리스트
class Wishlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE) # 작성자
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # 영화
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


# 예측
class Prediction(models.Model):
  source = models.ForeignKey(User, related_name = 'source_user', on_delete=models.CASCADE) # 평가를 요청한 사람
  target = models.ForeignKey(User, related_name = 'target_user', on_delete=models.CASCADE) # 평가를 받은 사람
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # 영화
  value = models.IntegerField() # 예측평점
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
