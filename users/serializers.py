from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
import json, pdb


class ProfileSerializer(serializers.ModelSerializer):
    uid = serializers.ReadOnlyField(source='user.id')
    name = serializers.ReadOnlyField(source='user.username')
    closeRate = serializers.SerializerMethodField()

    class Meta:
        model=Profile
        fields = ('uid', 'image', 'name', 'closeRate', 'badges')
    
    def get_closeRate(self, obj):
        current_user = obj.user
        intimacy = UserFriend.objects.filter(source=current_user).values_list('intimacy', flat=True).first()
        return intimacy