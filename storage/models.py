from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200 null=true)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatFied()
    digital = models.BooleanField(default=False, null=true, blank=True)

    def __str__(self):
        return self.name
