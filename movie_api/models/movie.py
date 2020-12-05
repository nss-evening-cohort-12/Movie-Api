from django.db import models
from django.db.models.deletion import CASCADE

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.ForeignKey("Rating", on_delete=CASCADE)
    director = models.ForeignKey("Director", on_delete=CASCADE, related_name="movies", related_query_name="movie")
    genre = models.ForeignKey("Genre", on_delete=CASCADE, related_name="movies", related_query_name="movie")
    actors = models.ManyToManyField("Actor", related_name="movies", related_query_name="movie")

    @property
    def average_rating(self):
        reviews = self.review_set.all()
        if len(reviews):
            return sum(review.rating for review in reviews) / len(reviews)
        return None
