from django.db import models
from django.utils import timezone

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)

    ticker = models.CharField(max_length=10)
    price = models.CharField(max_length=10)
    change = models.CharField(max_length=50)
    price_to_earn = models.CharField(max_length=50,default='10')

    time = models.DateTimeField(default=timezone.now)
