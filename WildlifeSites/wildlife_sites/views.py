from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    def get(self, request, *args, **kwargs):

        return render(request, "index.html", {})


def species_list(request):
    return render(request, 'wildlife_sites/species_list.html', {})