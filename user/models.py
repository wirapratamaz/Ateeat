from django.db import models

## BuyerUser
class BuyerUser(models.Model):
    authority = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=320)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()