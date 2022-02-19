from xml.parsers.expat import model
from django.db import models
from datetime import date

# Create your models here.
class Customer(models.Model):
    customerId = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    
    class Meta:
        db_table = "customer_details"    