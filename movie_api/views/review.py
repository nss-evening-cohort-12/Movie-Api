from rest_framework import viewsets
from movie_api.models import Review
from movie_api.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Reviews.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
