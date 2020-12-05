from rest_framework import viewsets
from movie_api.models import Director
from movie_api.serializers import DirectorSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Directors.
    """
    queryset = Director.objects.all()
    serializer_class =DirectorSerializer
