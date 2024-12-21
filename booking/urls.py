from django.urls import path
from .views import InterviewCreateView

app_name = 'booking'

urlpatterns =[
    path('create-interview/<int:pk>/', InterviewCreateView.as_view(), name='interview-create'),
]