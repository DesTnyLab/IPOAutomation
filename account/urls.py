# accounts/urls.py
from django.urls import path
from . views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('create/', create_account, name='create'),
    path("accounts/", AccountView.as_view(), name="home"),
    path("index/", index, name="index"),
    path("<int:account_id>/delete/", delete_Account, name="delete_account"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("docs/", docs, name="docs"),

] # Home page after login
