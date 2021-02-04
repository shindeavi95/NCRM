from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(default ="man.jpg" ,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
   
    def __str__(self):            # this is used for name visibility in admin panal
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):            # this is used for name visibility in admin
        return self.name


class Product(models.Model):
    CATEGORY = (
        ("Indoor", "Indoor"),     #  this is used for dropdown menu for category
        ("Out Door", "Out Door"),  # name = ((),())
        
    )
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True, choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)  
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)  

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (                          #  this is used for dropdown menu for status
        ("Pending","Pending"),
        ("Out for delivery","Out for delivery"),
        ("Delivered","Delivered"),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete = models.SET_NULL)
    product =  models.ForeignKey(Product, null=True, on_delete = models.SET_NULL) 

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.product.name