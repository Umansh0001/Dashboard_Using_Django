from django.db import models

class Search(models.Model):
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.pincode

class LocationData(models.Model):
    application_id = models.CharField(max_length=100, default='DEFAULT_ID')
    loan_account_number = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    area_type = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.product