from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("report.urls")),  # Make sure the report app has a urls.py
]
