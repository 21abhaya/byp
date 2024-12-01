from django.urls import path
from .views import PhotographerListView, PhotographerDetailView

app_name = 'photographer'

urlpatterns=[
    path('', PhotographerListView.as_view(), name='photographers'),
    path('photographer/<int:pk>/', PhotographerDetailView.as_view(), name='photographer-detail'),
]