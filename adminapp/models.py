from django.db import models

# Create your models here.

class Notification(models.Model):
    notification=models.TextField()
    posteddate=models.CharField(max_length=30)
class Rally(models.Model):
    location=models.CharField(max_length=500)
    rallydate=models.CharField(max_length=30)
    rallyfile=models.FileField()
class Result(models.Model):
    resultdate=models.CharField(max_length=30)
    resultfile=models.FileField()
