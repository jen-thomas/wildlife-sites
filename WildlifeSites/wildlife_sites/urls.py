from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.species_list, name='species_list'),
]