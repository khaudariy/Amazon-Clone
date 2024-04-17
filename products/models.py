from django.db import models
from taggit.managers import TaggableManager





# Create your models here.
FLAGS_TYPES=(('New','New'),('Sale','Sale'),('Feature','Feature'))




class Product(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=10,choices=FLAGS_TYPES)
    price =models.FloatField()
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=50000)
    tags = TaggableManager()
