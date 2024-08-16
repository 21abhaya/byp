from django.db import models
from photographer.models import Photographer
from customer.models import Customer

class Booking(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    scheduled_by = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, verbose_name="Client")
    scheduled_with = models.OneToOneField(Photographer, on_delete=models.SET_NULL, null=True, verbose_name="Photographer")
    scheduled_on = models.DateTimeField()

    class Meta:
        abstract = True

class Interview(Booking):
    TYPE=[
        ('In person','In person')
        ('Virtual','Virtual')
    ]
    interview_type = models.CharField(max_length=35, choices=TYPE, default='In Person')

class Photoshoot(Booking):
    venue = models.CharField(max=255, null=True, help_text="Location of the photoshoot venue")
