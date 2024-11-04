from django.views.generic import ListView, DetailView
from .models import Photographer

class PhotographerListView(ListView):
    model = Photographer
    template_name = 'photographer/photographer_list.html'
    context_object_name = 'photographers'