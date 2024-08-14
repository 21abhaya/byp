from django.db import models

class Portfolio(models.Model):
    images = models.ImageField(upload_to='portfolio/')

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
    category = models.CharField(max_length=1000, choices=PHOTOGRAPHY_GENRE, null=True)
    portfolio = models.OneToOneField(Portfolio,on_delete=models.SET_NULL, null=True)
    rate = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default=True)

    def __str__(self):

        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name
    
