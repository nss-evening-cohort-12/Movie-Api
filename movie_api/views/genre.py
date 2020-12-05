from rest_framework import viewsets
from movie_api.models import Genre
from movie_api.serializers import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Genres.
    """
    queryset = Genre.objects.all()
    serializer_class =GenreSerializer
