from django.shortcuts import render
from .models import Species
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    def get(self, request, *args, **kwargs):

        return render(request, "index.html", {})


def species_list(request):
    return render(request, 'wildlife_sites/species_list.html', {})

def species_list(request):
    species = Species.objects.all().order_by('common_name_english')
    return render(request, 'wildlife_sites/species_list.html', {'species': species})