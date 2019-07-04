from django.db import models

# Create your models here.
class BookInfo(models.Model):
    title=models.CharField(max_length=100)
class figureInfo(models.Model):
    gender=models.CharField(max_length=3)
    content=models.CharField(max_length=3)

