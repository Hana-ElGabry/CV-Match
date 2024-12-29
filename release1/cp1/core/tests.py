from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages


class UserAuthTests(TestCase):
    def setUp(self):
        # Set up a test client
        self.client = Client() #simulate HTTP requests

        # Create a test user
        self.test_user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_home_view(self):
        # Test if the home page loads successfully
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_register_view_success(self):
        # Test successful user registration
        response = self.client.post(reverse('register'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after registration
        self.assertTrue(User.objects.filter(username='johndoe').exists())

    def test_register_view_username_taken(self):
        response = self.client.post(reverse('register'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': 'testuser',  # Existing username
            'email': 'janedoe@example.com',
            'password': 'anotherpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect back to register page
        self.assertRedirects(response, reverse('register'))  # Ensure redirection happens

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Username already exists" in str(message) for message in messages))

    def test_login_view_success(self):
        # Test successful login
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect after login

    def test_login_view_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect back to login page
        self.assertRedirects(response, reverse('login'))  # Ensure redirection happens

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any("Invalid login credentials" in str(message) for message in messages))
