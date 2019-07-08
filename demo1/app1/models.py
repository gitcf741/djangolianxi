from django.db import models

# Create your models here.
class Questions(models.Model):
    title=models.CharField(max_length=30)
    creat_time=models.DateTimeField(auto_now_add=True)

class Chiose(models.Model):
    title=models.CharField(max_length=30)
    number=models.IntegerField(default=0)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)

