from rest_framework import serializers
from movie_api.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'description', 'user', 'rating', 'movie')


    def validate_rating(self, value):
        if value > 5 or value < 0:
            raise serializers.ValidationError("Rating should be between 0 and 5")
        return value
