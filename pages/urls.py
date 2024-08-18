from django.urls import path
from pages.views import Homepage

urlpatterns = [
    path('#', Homepage.as_view(), name = 'homepage'),
]