from django.contrib import admin
from django.contrib.gis.admin.options import OSMGeoAdmin

import wildlife_sites.models

# Register your models here.
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('latin_name', 'common_name_english', 'common_name_catalan', 'common_name_spanish')
    ordering = ['common_name_english']
    search_fields = ('latin_name', 'common_name_english', 'common_name_catalan', 'common_name_spanish')


class SiteAdmin(OSMGeoAdmin):
    list_display = ('name', 'position', 'location', 'country')
    ordering = ('name', 'location', 'country')
    search_fields = ('name', 'location', 'country')


admin.site.register(wildlife_sites.models.Species, SpeciesAdmin)
admin.site.register(wildlife_sites.models.Site, SiteAdmin)