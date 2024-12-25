from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Photographer, Interview, Photoshoot, Booking


class InterviewCreateView(CreateView):
    model = Interview
    template_name = 'booking/create_booking.html'
    fields =['scheduled_on']
    context_object_name = 'booking'
    obj_id = id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photographer'] = Photographer.objects.all()
        return context
