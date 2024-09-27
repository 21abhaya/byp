from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photographer

class PhotographerDetailView(DetailView):
    model = Photographer
    
    context_object_name = 'photographer'
class PhotographerListView(ListView):
    model = Photographer
    
    context_object_name = 'photographer_list'

# Create your views here.
