# accounts/urls.py
from django.urls import path
from . views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('create/', create_account, name='create'),
    path("", AccountView.as_view(), name="home"),
    path("<int:account_id>/delete/", delete_Account, name="delete_account"),
] # Home page after login
