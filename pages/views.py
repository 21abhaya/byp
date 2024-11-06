from django.shortcuts import render
from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = 'frontend/homepage.html'
    
    
class About(TemplateView):
    template_name = 'frontend/about.html'


class Blogs(TemplateView):
    template_name = 'frontend/blogs.html'
