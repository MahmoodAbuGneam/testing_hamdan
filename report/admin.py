from django.contrib import admin

# Register your models here.
# report/admin.py

from django.contrib import admin
from .models import Report  # Import your model

# Register your models here
admin.site.register(Report)
