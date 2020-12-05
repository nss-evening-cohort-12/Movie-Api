from django.contrib import admin
from movie_api.models import Actor, Director, Movie, Rating, Review, Genre

# Register your models here.
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(Review)
admin.site.register(Genre)

