"""The model for the Inquiry object."""
from django.db import models

class Inquiry(models.Model):
    """ Inquiry Model"""
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    remarks = models.TextField()

    def __str__(self):
        """Return the name of the inquiry."""
        return self.name

# Create your models here.
