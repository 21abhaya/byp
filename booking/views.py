from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Photographer, Interview, Photoshoot, Booking
from .forms import InterviewCreateForm

class InterviewCreateView(LoginRequiredMixin, CreateView):
    model = Interview
    template_name = 'booking/create_booking.html'
    form = InterviewCreateForm
    fields = '__all__'