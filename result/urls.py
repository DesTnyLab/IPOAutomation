
#urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_account, name='home'),
    path('<int:account_id>/', views.view_results, name='view-results'),
]   