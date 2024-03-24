from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=true)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=true, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)  #many to one relationship
    date_ordered = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False) #changes the status of the cart
    transaction_id = models.CharField(max_length=100, null=true)

    def __str__(self):
        return str(self.id)


#Items that need to be added to our order with a many to one relationship with our order

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null= True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

# This model will be a child to order and will only be created if at the ordertime within an order is physical product(if product.digital=False)
 
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)  #many to one relationship
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length==200, null=False)
    state = models.CharField(max_length==200, null=False)
    zipcode = models.CharField(max_length==200, null=False)

    def __str__(self):
        return self.address


