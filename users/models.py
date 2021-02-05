from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# 뱃지
class Badge(models.Model):
  name = models.CharField(max_length=100) # 이름
  description = models.TextField(blank=True) # 설명
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  
# User 모델과 대응하는 프로필(프로필 사진을 등록하기 위함)
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.TextField(default="https://avatars.githubusercontent.com/u/78534587?s=200&v=4") # 프로필 사진
  friends = models.ManyToManyField("self", through="UserFriend", symmetrical=False)
  badges = models.ManyToManyField(Badge)

  @receiver(post_save, sender=User)
  def create_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)

          other_users = User.objects.all()
          current_user = instance
          for user in other_users: # Note: 자기 자신을 제외한 모든이와 친구
              if user != current_user:
                  UserFriend.objects.create(source=instance, target=user, intimacy=0)
                  UserFriend.objects.create(source=user, target=instance, intimacy=0)

  @receiver(post_save, sender=User)
  def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()


class UserFriend(models.Model):
  source = models.ForeignKey(User, related_name = 'source', on_delete=models.CASCADE)
  target = models.ForeignKey(User, related_name = 'target', on_delete=models.CASCADE)
  intimacy = models.IntegerField() # 관계점수



