from django.db import models
# from django.contrib.gis.db import models


class Idea(models.Model):
    place = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.place


class Location(models.Model):
    idea_text = models.ForeignKey(Idea, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.name
