from django.db import models
from photographer.models import Photographer
from customer.models import Customer

class Booking(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    scheduled_by = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, verbose_name="Client")
    scheduled_with = models.OneToOneField(Photographer, on_delete=models.SET_NULL, null=True, verbose_name="Photographer")
    scheduled_on = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['created_on']

    def __str__(self):
        return f"Booking on {self.scheduled_on} with {self.scheduled_with}"

class Interview(Booking):
    TYPE = [
        ('In person','In person'),
        ('Virtual','Virtual'),
    ]
    interview_type = models.CharField(max_length=35, choices=TYPE, default='In Person')

    def __str__(self):
        return f"{self.interview_type} Interview on {self.scheduled_on}"

class Photoshoot(Booking):
    venue = models.CharField(max_length=255, null=True, help_text="Location of the photoshoot venue")

    def __str__(self):
        return f"Photoshoot at {self.venue} on {self.scheduled_on}"