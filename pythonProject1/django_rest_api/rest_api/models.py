from ast import Mod
# from distutils.command.upload import upload
# import email
from itertools import product
from pyexpat import model
# from unicodedata import category, name
from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)
    address = models.TextField(max_length=500)
    phone = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)



class Store(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=500)
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.CharField(max_length=300)
    price = models.IntegerField()
    stock = models.IntegerField()
    condition = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)

class ProductImg(models.Model):
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    category = models.CharField(max_length=300)


class Cart(models.Model):
    userId= models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CartItem(models.Model):
    cartId= models.ForeignKey(Cart,on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


def upload_location(instance, filename):
    ext = filename.Split(".")[-1]
    return "%s/%s.%s"("img",datetime.now(), ext)
class FileUpload(models.Model):
    imgFile= models.ImageField(upload_to=upload_location)
    


   
    
