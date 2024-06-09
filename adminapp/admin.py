
from django.contrib import admin
from . models import Notification, Rally, Result

# Register your models here.
admin.site.register(Notification)
admin.site.register(Rally)
admin.site.register(Result)
