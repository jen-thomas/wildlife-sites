from django.contrib.gis.db import models

# Create your models here.
class Species(models.Model):
    latin_name = models.CharField(max_length=1024)
    common_name_english = models.CharField(max_length=1024)
    common_name_catalan = models.CharField(max_length=1024)
    common_name_spanish = models.CharField(max_length=1024)

    def __str__(self):
        return "{}".format(self.common_name_english)


class Site(models.Model):
    name = models.CharField(max_length=1024)
    position = models.PointField(null=True, blank=True)
    location = models.CharField(max_length=512)
    country = models.CharField(max_length=256)
    notes = models.TextField(max_length=1024)

    def __str__(self):
        return "{}".format(self.name)

    def latitude(self):
        return self.location.y

    def longitude(self):
        return self.location.x