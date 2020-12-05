from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    description = models.TextField()
    movie = models.ForeignKey("Movie", on_delete=CASCADE)
    rating = models.IntegerField()
