from django.db import models

class Voucher(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField() 
    capacity = models.IntegerField()
    staged = models.BooleanField()                                                                 
    vouchtype = models.TextField()
    vouchvalue = models.TextField()

class Product(models.Model):
	title = models.CharField(max_length=20)
	price = models.FloatField()

class Order(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()

class History(models.Model):
    orders = models.TextField()
    payout = models.FloatField()
    date = models.DateField()
