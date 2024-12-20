from django.shortcuts import render, redirect

from .models import Report
from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report

def report_issue(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            # Get the location (latitude, longitude) from the form
            location = request.POST.get('location')
            if location:
                # Split the location into latitude and longitude
                latitude, longitude = map(float, location.split(','))
                form.instance.latitude = latitude
                form.instance.longitude = longitude

            # Save the form data (including the location)
            form.save()

            return redirect('home')  # Adjust to your success page
    else:
        form = ReportForm()

    return render(request, 'report_problem.html', {'form': form})
from django.shortcuts import render
from .models import Report

def home(request):
    reports = Report.objects.all()  # Get all reports
    return render(request, 'home.html', {'reports': reports})

from django.http import JsonResponse
from .models import Report

def delete_report(request, report_id):
    if request.method == "POST":
        try:
            report = Report.objects.get(id=report_id)
            report.delete()
            return JsonResponse({"success": True})
        except Report.DoesNotExist:
            return JsonResponse({"success": False, "error": "Report not found."})
    return JsonResponse({"success": False, "error": "Invalid request."})
