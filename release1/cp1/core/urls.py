from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.RegisterView, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/download/<str:doc_type>/', views.download_document, name='download_document'),
    path('download_pdf/<int:user_id>/', views.download_pdf, name='download_pdf'),
    path('download_word/<int:user_id>/', views.download_word, name='download_word'),
]