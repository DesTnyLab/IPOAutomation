# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('create_account/', views.create_account, name='create_account'),
    path('', views.home, name='home'),  # Home page after login
]
