from django.db import models

# Create your models here.
class Species(models.Model):
    latin_name = models.CharField(max_length=1024)
    common_name_english = models.CharField(max_length=1024)
    common_name_catalan = models.CharField(max_length=1024)
    common_name_spanish = models.CharField(max_length=1024)

    def __str__(self):
        return "{}".format(self.common_name_english)