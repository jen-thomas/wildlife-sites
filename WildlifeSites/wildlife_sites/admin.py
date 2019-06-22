from django.contrib import admin

import wildlife_sites.models

# Register your models here.
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('latin_name', 'common_name_english', 'common_name_catalan', 'common_name_spanish')
    ordering = ['common_name_english']
    search_fields = ('latin_name', 'common_name_english', 'common_name_catalan', 'common_name_spanish')


admin.site.register(wildlife_sites.models.Species, SpeciesAdmin)