from django.contrib import admin
from django.contrib.gis.admin.options import OSMGeoAdmin

import wildlife_sites.models

# Register your models here.

class TaxonomyClassAdmin(admin.ModelAdmin):
    list_display = ('taxclass',)
    ordering = ('taxclass',)
    search_fields = ('taxclass',)


class TaxonomyOrderAdmin(admin.ModelAdmin):
    list_display = ('taxclass', 'order')
    ordering = ('taxclass', 'order')
    search_fields = ('taxclass', 'order')


class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('latin_name', 'order')
    ordering = ('latin_name', 'order')
    search_fields = ('latin_name', 'order')


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('latin_name', 'common_name_english', 'common_name_catalan', 'common_name_spanish')
    ordering = ['common_name_english']
    search_fields = ('latin_name', 'common_name_english', 'common_name_catalan', 'common_name_spanish')


class SiteAdmin(OSMGeoAdmin):
    list_display = ('name', 'position', 'location', 'country')
    ordering = ('name', 'location', 'country')
    search_fields = ('name', 'location', 'country')


class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    ordering = ('type',)
    search_fields = ('type',)


class UriTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    ordering = ('type',)
    search_fields = ('type',)


class UriAdmin(admin.ModelAdmin):
    list_display = ('uri', 'uri_type')
    ordering = ('uri', 'uri_type')
    search_fields = ('uri', 'uri_type')


class ReferenceTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    ordering = ('type',)
    search_fields = ('type',)


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('reference', 'reference_type')
    ordering = ('reference', 'reference_type')
    search_fields = ('reference', 'reference_type')


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'source_type', 'uri', 'reference')
    ordering = ('title', 'author', 'source_type', 'uri', 'reference')
    search_fields = ('title', 'author', 'source_type', 'uri', 'reference')


class TimeOfYearAdmin(admin.ModelAdmin):
    list_display = ('month',)
    ordering = ('month',)
    search_fields = ('month',)


class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ('site', 'species', 'months', 'source')
    ordering = ('site', 'species', 'time_of_year', 'source')
    search_fields = ('site', 'species', 'time_of_year', 'source')


admin.site.register(wildlife_sites.models.TaxonomyClass, TaxonomyClassAdmin)
admin.site.register(wildlife_sites.models.TaxonomyOrder, TaxonomyOrderAdmin)
admin.site.register(wildlife_sites.models.Taxonomy, TaxonomyAdmin)
admin.site.register(wildlife_sites.models.Species, SpeciesAdmin)
admin.site.register(wildlife_sites.models.Site, SiteAdmin)
admin.site.register(wildlife_sites.models.SourceType, SourceTypeAdmin)
admin.site.register(wildlife_sites.models.UriType, UriTypeAdmin)
admin.site.register(wildlife_sites.models.Uri, UriAdmin)
admin.site.register(wildlife_sites.models.ReferenceType, ReferenceTypeAdmin)
admin.site.register(wildlife_sites.models.Reference, ReferenceAdmin)
admin.site.register(wildlife_sites.models.Source, SourceAdmin)
admin.site.register(wildlife_sites.models.TimeOfYear, TimeOfYearAdmin)
admin.site.register(wildlife_sites.models.SiteVisit, SiteVisitAdmin)