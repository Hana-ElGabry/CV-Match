# filepath: tests/test_login.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTest(TestCase):
    def setUp(self):
        # Set up a test user
        self.username = "testuser"
        self.password = "password123"
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.login_url = reverse('login')  # Adjust the URL name to match your login view

    def test_login_success(self):
        # Test a successful login
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': self.password,
        })
        self.assertEqual(response.status_code, 200)  # Assuming success returns HTTP 200
        self.assertContains(response, "Welcome, testuser")  # Example success message

    def test_login_failure(self):
        # Test a failed login
        response = self.client.post(self.login_url, {
            'username': self.username,
            'password': "wrongpassword",
        })
        self.assertEqual(response.status_code, 401)  # Assuming failure returns HTTP 401
        self.assertContains(response, "Invalid credentials")  # Example error message
