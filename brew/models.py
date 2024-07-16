from django.db import models

# Create your models here.
class Coffee(models.Model):
    type = models.CharField(max_length=200)
    temperature = models.CharField(max_length=500)
    caffeine_amount = models.CharField(max_length=200)
    price = models.CharField(max_length=500)

class Snack(models.Model):
    type = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=500) 