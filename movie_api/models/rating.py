from django.db import models

class Rating(models.Model):
    label = models.CharField(max_length=10)
