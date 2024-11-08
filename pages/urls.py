from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.Homepage.as_view(), name = 'homepage'),
    path('about/', views.About.as_view(), name = 'about'),
    path('blogs/', views.Blogs.as_view(), name = 'blogs'),
    path('login/', views.Login.as_view(), name = 'login'),
    path('register/', views.SignUp.as_view(), name='register'),
]
