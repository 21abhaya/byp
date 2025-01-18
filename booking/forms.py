from django import forms
from django.forms import ModelForm
from .models import Interview, Photoshoot, Photographer

class InterviewCreateForm(forms.ModelForm):
    model = Interview
    fields='__all__'
    
