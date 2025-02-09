from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Photographer, Interview, Photoshoot, Booking
from .forms import InterviewCreateForm

class InterviewCreateView(CreateView):
    model = Interview
    template_name = 'booking/create_booking.html'
    form = InterviewCreateForm
    fields = '__all__'