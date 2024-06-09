from django.shortcuts import render, redirect
from ARZapp.models import AdminLogin, Enquiry ,UserInfo
from django.views.decorators.cache import cache_control
import datetime
from . models import Notification, Rally, Result
# Create your views here.
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            obj=AdminLogin.objects.get(adminid=adminid)
            return render(request,"adminhome.html",locals())
    except KeyError:
        return redirect("Adminlogin")
    
def response(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            obj=AdminLogin.objects.get(adminid=adminid)
            enq=Enquiry.objects.all()
            return render(request,"response.html",locals())
    except KeyError:
        return redirect("Adminlogin")
    
def delenq(request,id):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            obj=AdminLogin.objects.get(adminid=adminid)
            enq=Enquiry.objects.all()
            enq=Enquiry.objects.get(id=id)
            enq.delete()
            return render(request,"adminhome.html",locals())
    except KeyError:
        return redirect("Adminlogin")
    
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def changepassword(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            if request.method=="POST":
                oldpassword=request.POST['oldpassword']
                newpassword=request.POST['newpassword']
                cnfpassword=request.POST['cnfpassword']
                obj=AdminLogin.objects.get(adminid=adminid)
                if newpassword!=cnfpassword:
                    msg="Enter same password"
                elif obj.password!=oldpassword:
                    msg="Enter correct password"
                elif obj.password==oldpassword:
                    AdminLogin.objects.filter(adminid=adminid).update(password=newpassword)
                    return redirect("ARZapp:adminlogin")
                return render(request,"changepassword.html",locals())
            return render(request,"changepassword.html",locals())
    except KeyError:
        return redirect("adminapp:login")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def addnotification(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            note = Notification.objects.all()
            if request.method=="POST":
                addnotification=request.POST['addnotification']
                posteddate=datetime.datetime.today()
                noti=Notification(notification=addnotification,posteddate=posteddate)
                noti.save()
                msg="Notification is added"
                return render(request,"addnotification.html",locals())
            return render(request,"addnotification.html",locals())
    except KeyError:
        return redirect("adminapp:login")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def addrally(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            ral = Rally.objects.all()
            if request.method=="POST":
                location=request.POST['location']
                rallyfile=request.FILES['rallyfile']
                rallydate=datetime.datetime.today()
                ral=Rally(location=location,rallydate=rallydate,rallyfile=rallyfile)
                ral.save()
                msg="Added"
                ral = Rally.objects.all()
                return render(request,"addrally.html",locals())
            return render(request,"addrally.html",locals())
    except KeyError:
        return redirect("adminapp:login")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def resultmanagement(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            rel=Result.objects.all()
            if request.method=="POST":
                resultfile=request.FILES['resultfile']
                resultdate=datetime.datetime.today()
                result=Result(resultdate=resultdate,resultfile=resultfile)
                result.save()
                return redirect("adminapp:resultmanagement")
            return render(request,"resultmanagement.html",locals())
    except KeyError:
        return redirect("adminapp:login")

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def userregister(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            user=UserInfo.objects.all()
            return render(request,"userregister.html",locals())
    except KeyError:
        return redirect("adminapp:login")


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
    try:
        del request.session["adminid"]
        return redirect("ARZapp:adminlogin")
    except KeyError:
        return redirect("ARZapp:login")
    return redirect("ARZapp:login")

def delnote(request,id):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            Notification.objects.get(id=id).delete()
            return redirect("adminapp:addnotification")
    except KeyError:
        return redirect("Adminlogin")
    
def delral(request,id):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            Rally.objects.get(id=id).delete()
            return redirect("adminapp:addrally")
    except KeyError:
        return redirect("Adminlogin")

def delrel(request,id):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            Result.objects.get(id=id).delete()
            return redirect("adminapp:resultmanagement")
    except KeyError:
        return redirect("Adminlogin")
