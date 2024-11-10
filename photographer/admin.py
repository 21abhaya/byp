from django.contrib import admin
from .models import Photographer, Portfolio, Rating, Review

admin.site.register(Photographer)
admin.site.register(Portfolio)
admin.site.register(Rating)
admin.site.register(Review)
