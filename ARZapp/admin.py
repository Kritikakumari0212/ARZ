from django.contrib import admin
from . models import Enquiry, UserInfo, AdminLogin

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(UserInfo)
admin.site.register(AdminLogin)
