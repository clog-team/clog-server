from rest_framework import serializers
from .models import *
import json


class PredictionSerializer(serializers.ModelSerializer):
    movieCode = serializers.ReadOnlyField(source='movie.movie_code')
    thumbnailUrl = serializers.ReadOnlyField(source='movie.thumbnail_url')
    movieName = serializers.ReadOnlyField(source='movie.title')
    directors = serializers.SerializerMethodField()
    openingDate = serializers.ReadOnlyField(source='movie.opening_date')
    genre = serializers.ReadOnlyField(source='movie.genre')
    runningTime = serializers.ReadOnlyField(source='movie.running_time')

    class Meta:
        model = Prediction
        fields = ('movieCode', 'thumbnailUrl', 'movieName', 'directors', 'openingDate', 'genre', 'runningTime')
    
    def get_directors(self, obj):
        return json.loads(obj.movie.directors)

    def to_representation(self, obj):
        data = super(PredictionSerializer, self).to_representation(obj)
        return {
          "movie": data,
          "friendUserId": obj.source.id
        }