from django.contrib import admin
from .models import Startup,CustomUser

# Register your models here.
admin.site.register(Startup)
admin.site.register(CustomUser)