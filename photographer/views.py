from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Photographer, Portfolio, Rating

class PhotographerListView(ListView):
    model = Photographer
    template_name = 'photographer/photographer_list.html'
    paginate_by = 12
    context_object_name = 'photographers'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search')
        if search_term:
            queryset=queryset.filter(
                Q(first_name__icontains=search_term)|
                Q(last_name__icontains=search_term)|
                Q(category__icontains=search_term)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.model.objects.all()
        search_term = self.request.GET.get('search')
        if search_term:
            queryset=queryset.filter(
                Q(first_name__icontains=search_term)|
                Q(last_name__icontains=search_term)|
                Q(category__icontains=search_term)
            ) 
            if not queryset.exists():
                context['no_results']=f'No match found for "{search_term}"'  
        return context
    

class PhotographerDetailView(DetailView):
    model = Photographer
    template_name = "photographer/photographer_detail.html"
 