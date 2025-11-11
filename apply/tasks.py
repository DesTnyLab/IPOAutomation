# # app/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import CompanyShare




@shared_task
def print_hello():
    print("Hello, World!")


