from django.urls import path
from .views import PhotographerListView

app_name = 'photographer'

urlpatterns=[
    path('', PhotographerListView.as_view(), name='photographers'),
]