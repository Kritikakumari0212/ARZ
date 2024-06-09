from django.shortcuts import render, redirect
from . models import Enquiry, UserInfo, AdminLogin
import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminapp.models import Result,Rally,Notification
# Create your views here.
def index(request):
    notice=Notification.objects.all()
    return render(request,"index.html",locals())

def contactus(request):
    if request.method=="POST":
        name= request.POST['name']
        contactno= request.POST['contactno']
        emailaddress= request.POST['emailaddress']
        address= request.POST['address']
        subject= request.POST['subject']
        message= request.POST['message']
        posteddate = datetime.datetime.now()
        enq= Enquiry(name=name,contactno=contactno,emailaddress=emailaddress, address=address,subject=subject, message=message, posteddate=posteddate)
        enq.save()
        msg="your enquiry is submitted successfully"
        return render(request,"contactus.html",{"msg":msg})
    return render(request,"contactus.html")

def registration(request):
    if request.method=="POST":
        name= request.POST['name']
        gender= request.POST['gender']
        address= request.POST['address']
        city= request.POST['city']
        contactno= request.POST['contactno']
        emailaddress= request.POST['emailaddress']
        adharno= request.POST['adharno']
        panno= request.POST['panno']
        qualification= request.POST['qualification']
        dob= request.POST['dob']
        reg=UserInfo(name=name,gender=gender,address=address,city=city,contactno=contactno,emailaddress=emailaddress,aadharno=adharno,panno=panno,qualification=qualification,dob=dob)
        reg.save()
        msg="Registration is done"
        return render(request,"registration.html",{"msg":msg})
    return render(request,"registration.html")
def login(request):
    if request.method=="POST":
        adminid= request.POST['adminid']
        password= request.POST['password']
        try:
            obj= AdminLogin.objects.get(adminid=adminid,password=password)
            if obj is not None:
                request.session['adminid']=adminid
                return redirect("adminapp:adminhome")
        except ObjectDoesNotExist:
            msg="INVALID Credentials"
        return render(request,"adminlogin.html",{"msg":msg})
    return render(request,"adminlogin.html")
# def aboutus(request):
#     return render(request,"aboutus.html")

def viewresult(request):
    res=Result.objects.all()
    return render(request,"viewresult.html",locals())

def viewrally(request):
    ral=Rally.objects.all()
    return render(request,"viewrally.html",locals())

