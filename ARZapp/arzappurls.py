from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contactus/',views.contactus,name="contactus"),
    path('registration/',views.registration,name="registration"),
    path('adminlogin/',views.login,name="adminlogin"),
    # path('aboutus/',views.aboutus,name="aboutus"),
    path('viewresult/',views.viewresult,name="viewresult"),
    path('viewrally/',views.viewrally,name="viewrally"),
]