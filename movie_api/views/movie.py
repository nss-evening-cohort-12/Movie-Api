from django.http.response import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from movie_api.serializers import MovieCreateSerializer
from rest_framework import viewsets
from movie_api.models import Movie
from movie_api.serializers import MovieListSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def create(self, request):
        serializer = MovieCreateSerializer(data=request.data)
        if serializer.is_valid():
            actors = serializer.validated_data.pop('actors')
            movie = Movie.objects.create(**serializer.validated_data)
            for actor in actors:
                movie.actors.add(actor)

            serializer = MovieListSerializer(movie)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HttpResponseBadRequest.status_code)
