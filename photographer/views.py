from django.views.generic import ListView, DetailView
from .models import Photographer, Portfolio, Rating

class PhotographerListView(ListView):
    model = Photographer
    template_name = 'photographer/photographer_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photographers'] = Photographer.objects.all()
        context['ratings'] = Rating.objects.all()
        context['portfolios'] = Portfolio.objects.all()
        return context
    
    