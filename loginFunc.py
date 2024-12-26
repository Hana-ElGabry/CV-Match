import os
import django
from django.conf import settings
from django.http import HttpResponse
from django.test.client import RequestFactory
import pandas as pd

# Configure Django settings
BASE_DIR = os.getcwd()  # Use the current working directory
settings.configure(
    DEBUG=True,
    SECRET_KEY='your_secret_key',
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    },
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
)
django.setup()

# Simulate user data in a DataFrame (instead of reading from an Excel file)
data = {
    'username': ['testuser'],
    'password': ['testpassword']
}

# Create the DataFrame
users_df = pd.DataFrame(data)

# Function to simulate login from a DataFrame
def login_user(request):
    # Extract credentials from the request
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Check if the username exists in the DataFrame and password matches
    user = users_df[users_df['username'] == username]
    if not user.empty and user['password'].values[0] == password:
        return HttpResponse("Login successful")
    else:
        return HttpResponse("Invalid credentials")

# Simulate a request
factory = RequestFactory()
request = factory.post('/login/', {'username': 'testuser', 'password': 'testpassword'})

# Call the login function
response = login_user(request)
print(response.content.decode())
