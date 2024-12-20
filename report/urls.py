from django.urls import path
from . import views

urlpatterns = [
    path('report_problem/', views.report_issue, name='report_problem'),
    path('', views.home, name='home'),  # Home page shows the map with reports
path('delete_report/<int:report_id>/', views.delete_report, name='delete_report'),
]
