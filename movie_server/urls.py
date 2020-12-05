"""movie_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from movie_api.views import ActorViewSet
from movie_api.views import GenreViewSet
from movie_api.views import DirectorViewSet
from movie_api.views import MovieViewSet
from movie_api.views import RatingViewSet
from movie_api.views import ReviewViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'actors', ActorViewSet, 'actors')
router.register(r'directors', DirectorViewSet, 'director')
router.register(r'genres', GenreViewSet, 'genre')
router.register(r'movies', MovieViewSet, 'movie')
router.register(r'ratings', RatingViewSet, 'rating')
router.register(r'reviews', ReviewViewSet, 'review')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
