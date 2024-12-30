from django.db import models

class TransitAgency(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)#help_text="Enter the 2 letter abbreviation for the state where the Transit Agency is located")
    customer_account_number = models.CharField(max_length=20)#, help_text="Enter the customer account num")
class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50)  # Allow any input for vehicle type
    customer = models.CharField(max_length=100)  # Customer name
    build_manufacturer = models.CharField(max_length=100)  # Manufacturer name
    build_year = models.PositiveIntegerField()  # Year of manufacture
