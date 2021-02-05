from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
import json


class ProfileSerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField(source='user.id')
    name = serializers.ReadOnlyField(source='user.username')
    # closeRate = UserFriend.objects.filter(source=user, target=user5).get().intimacy

    class Meta:
        model=Profile
        fields = ('uid', 'image', 'name', 'badges')