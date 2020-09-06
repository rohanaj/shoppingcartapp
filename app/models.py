from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name =  models.CharField(max_length=80)
    description = models.TextField(max_length=100)
    photo = models.URLField()
    price = models.FloatField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    created_by = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
