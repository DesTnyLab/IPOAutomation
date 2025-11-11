
#urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_account, name='results'),
    path('<int:account_id>/', views.view_results, name='view-results'),
]   