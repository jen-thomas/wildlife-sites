from django.contrib.gis.db import models

# Create your models here.

class Taxonomy(models.Model):
    latin_name = models.CharField(max_length=255, unique=True)
    taxclass = models.CharField(max_length=256, name='class', null=True, blank=True)
    order = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.latin_name)


class Species(models.Model):
    latin_name = models.OneToOneField(Taxonomy, on_delete=models.PROTECT)
    common_name_english = models.CharField(max_length=1024, null=True, blank=True)
    common_name_catalan = models.CharField(max_length=1024, null=True, blank=True)
    common_name_spanish = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.common_name_english)


class Site(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position = models.PointField(null=True, blank=True)
    location = models.CharField(max_length=512)
    country = models.CharField(max_length=256)
    notes = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def latitude(self):
        return self.location.y

    def longitude(self):
        return self.location.x


class SourceType(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return "{}".format(self.type)


class UriType(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return "{}".format(self.type)


class Uri(models.Model):
    uri = models.CharField(max_length=1024)
    uri_type = models.ForeignKey(UriType, on_delete=models.PROTECT)

    def __str__(self):
        return "{}: {}".format(self.uri_type, self.uri)


class ReferenceType(models.Model):
    type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return "{}".format(self.type)


class Reference(models.Model):
    reference = models.CharField(max_length=1024)
    reference_type = models.ForeignKey(ReferenceType, on_delete=models.PROTECT)

    def __str__(self):
        return "{}: {}".format(self.reference_type, self.reference)


class Source(models.Model):
    title = models.CharField(max_length=1024)
    author = models.CharField(max_length=256, null=True, blank=True)
    source_type = models.ForeignKey(SourceType, on_delete=models.PROTECT)
    uri = models.OneToOneField(Uri, on_delete=models.PROTECT, null=True, blank=True)
    reference = models.ForeignKey(Reference, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return "{}: {}".format(self.source_type, self.title)


class TimeOfYear(models.Model):
    month = models.IntegerField(unique=True)

    def __str__(self):
        return "{}".format(self.month)


class SiteVisit(models.Model):
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    time_of_year = models.ManyToManyField(TimeOfYear, blank=True)
    source = models.ForeignKey(Source, on_delete=models.PROTECT, null=True, blank=True)

    def months(self):
        return ",".join([str(t) for t in self.time_of_year.all()])