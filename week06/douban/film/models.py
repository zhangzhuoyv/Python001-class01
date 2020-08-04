from django.db import models

# Create your models here.
from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_type = models.CharField(max_length=255)
    movie_showtime = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'movie'


class T1(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.FloatField()

    class Meta:
        managed = False
        db_table = 't1'
