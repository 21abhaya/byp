from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from customer.models import Customer

class Portfolio(models.Model):
    images = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return f"{self.images}"
    
    def get_absolute_url(self):
        return reverse('portfolio_detail', args=[str(self.id)])

class Rating(models.Model):
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    class Meta:
        ordering = ['rating']

    def __str__(self):
        return f"{self.rating}"

class Photographer(models.Model):
    PHOTOGRAPHY_GENRE = [
    ('Adventure Photography', 'Adventure Photography'),
    ('Aerial Photography', 'Aerial Photography'),
    ('Astro Photography', 'Astro Photography'),
    ('Automotive Photography', 'Automotive Photography'),
    ('Commercial Photography', 'Commercial Photography'),
    ('Documentary Photography', 'Documentary Photography'),
    ('Event Photography', 'Event Photography'),
    ('Fashion Photography', 'Fashion Photography'),
    ('Fine Art Photography', 'Fine Art Photography'),
    ('Food Photography', 'Food Photography'),
    ('Industrial Photography', 'Industrial Photography'),
    ('Landscape Photography', 'Landscape Photography'),
    ('Medical Photography', 'Medical Photography'),
    ('Pet Photography', 'Pet Photography'),
    ('Photojournalist', 'Photojournalist'),
    ('Portrait Photography', 'Portrait Photography'),
    ('Product Photography', 'Product Photography'),
    ('Real Estate Photography', 'Real Estate Photography'),
    ('Scientific Photography', 'Scientific Photography'),
    ('Sports Photography', 'Sports Photography'),
    ('Stock Photography', 'Stock Photography'),
    ('Street Photography', 'Street Photography'),
    ('Travel Photography', 'Travel Photography'),
    ('War Photography', 'War Photography'),
    ('Wedding Photography', 'Wedding Photography'),
    ('Wildlife Photography', 'Wildlife Photography'),
    ]
    first_name = models.CharField(max_length=50, help_text="Enter first name")
    last_name = models.CharField(max_length=50, help_text="Enter last name")
    email = models.EmailField(max_length=200, null=True)
    phone_no = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=1000, null=True)
    category = models.CharField(max_length=100, choices=PHOTOGRAPHY_GENRE, null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True)
    rating = models.ForeignKey(Rating, null=True, on_delete=models.SET_NULL)
    rate = models.CharField(max_length=100, blank=True, null=True, verbose_name='Fees')
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):

        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name
    
    def get_absolute_url(self):
        return reverse('photographer_detail', args=[str(self.id)])
    
class Review(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE, null=True)
    comments = models.TextField(max_length=1000, null=True)
    created_by = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment: {self.comment} by {self.created_by} for {self.photographer}"
    
    def get_absolute_url(self):
        return reverse('reiew_detail', args=[str(self.id)])
