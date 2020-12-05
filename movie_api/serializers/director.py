from rest_framework import serializers
from movie_api.models import Director

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')
