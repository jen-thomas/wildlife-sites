from django.urls import path
from . import views


urlpatterns = [
    path('', views.species_list, name='species_list'),
]