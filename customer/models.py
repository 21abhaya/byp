from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50, help_text="Enter first name")
    last_name = models.CharField(max_length=50, help_text="Enter last name")
    email = models.EmailField(max_length=200, null=True)
    phone_no = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=255, null=True)


    def __str__(self):

        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name
    
