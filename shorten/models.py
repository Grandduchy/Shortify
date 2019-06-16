from django.db import models

# Create your models here.

class Url(models.Model):
    url = models.CharField(max_length=300)
    shortenUrl = models.CharField(max_length=50)
    dateAdded = models.DateTimeField(auto_now_add=True)

