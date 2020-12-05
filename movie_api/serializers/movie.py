from rest_framework import serializers
from movie_api.models import Movie

class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'genre', 'director', 'actors', 'rating')
       

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'year', 'genre', 'director', 'actors', 'rating', 'average_rating')
        depth = 1
