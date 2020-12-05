from rest_framework import viewsets
from movie_api.models import Rating
from movie_api.serializers import RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Ratings.
    """
    queryset = Rating.objects.all()
    serializer_class =RatingSerializer
