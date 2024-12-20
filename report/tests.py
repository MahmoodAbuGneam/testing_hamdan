from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Report
import json

class ReportDeletionTests(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()
        # Create a test report with the correct fields
        self.report = Report.objects.create(
            name="Test User",
            email="test@example.com",
            phone_number="1234567890",
            description="Test Description",
            latitude=40.7128,
            longitude=-74.0060
        )

    def test_successful_report_deletion(self):
        # Get the initial count of reports
        initial_count = Report.objects.count()
        
        # Make a POST request to delete the report
        response = self.client.post(reverse('delete_report', args=[self.report.id]))
        
        # Check if the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Parse the JSON response
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        
        # Check if the report was actually deleted
        self.assertEqual(Report.objects.count(), initial_count - 1)
        
        # Verify the report no longer exists in the database
        with self.assertRaises(Report.DoesNotExist):
            Report.objects.get(id=self.report.id)

    def test_delete_nonexistent_report(self):
        # Try to delete a report that doesn't exist
        non_existent_id = 99999
        response = self.client.post(reverse('delete_report', args=[non_existent_id]))
        
        # Check if the response is successful but indicates failure
        self.assertEqual(response.status_code, 200)
        
        # Parse the JSON response
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], "Report not found.")

    def test_delete_report_with_get_method(self):
        # Try to delete with GET method instead of POST
        response = self.client.get(reverse('delete_report', args=[self.report.id]))
        
        # Check if the response indicates failure
        self.assertEqual(response.status_code, 200)
        
        # Parse the JSON response
        data = json.loads(response.content)
        self.assertFalse(data['success'])
        self.assertEqual(data['error'], "Invalid request.")
        
        # Verify the report still exists
        self.assertTrue(Report.objects.filter(id=self.report.id).exists())
