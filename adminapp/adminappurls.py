from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name="adminhome"),
    path('addnotification/',views.addnotification,name="addnotification"),
    path('addrally/',views.addrally,name="addrally"),
    path('resultmanagement/',views.resultmanagement,name="resultmanagement"),
    path('logout/',views.logout,name="logout"),
    path('userregister/',views.userregister,name="userregister"),
    path('response/',views.response,name="response"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('delenq/<id>',views.delenq,name="delenq"),
    path('delral/<id>',views.delral,name="delral"),
    path('delnote/<id>',views.delnote,name="delnote"),
    path('delrel/<id>',views.delrel,name="delrel"),
]