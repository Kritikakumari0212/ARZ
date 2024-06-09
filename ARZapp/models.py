from django.db import models

# Create your models here.

class Enquiry(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contactno= models.CharField(max_length=10)
    emailaddress= models.CharField(max_length=50)
    address= models.CharField(max_length=500)
    subject= models.CharField(max_length=100)
    message= models.TextField()
    posteddate= models.CharField(max_length=30)
    

class UserInfo(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    city=models.CharField(max_length=50)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50,primary_key=True)
    aadharno=models.CharField(max_length=12)
    panno=models.CharField(max_length=10)
    qualification=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
class AdminLogin(models.Model):
    adminid=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=20)
