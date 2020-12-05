from rest_framework import viewsets
from movie_api.models import Actor
from movie_api.serializers import ActorSerializer

class ActorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Actors.
    """
    queryset = Actor.objects.all()
    serializer_class =ActorSerializer
