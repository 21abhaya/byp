from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

class Homepage(TemplateView):
    template_name = 'frontend/homepage.html'
    
    
class About(TemplateView):
    template_name = 'frontend/about.html'


class Blogs(TemplateView):
    template_name = 'frontend/blogs.html'

class Login(LoginView):
    template_name = 'frontend/login.html'

class SignUp(TemplateView):
    template_name = 'frontend/signup.html'
