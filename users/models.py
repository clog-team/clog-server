from django.contrib.auth.models import User
from django.db import models

# User 모델과 대응하는 프로필(프로필 사진을 등록하기 위함)
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(verbose_name="Image of User", upload_to="image/", default="movie-it-logo.png")

# 뱃지
class Badge(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
