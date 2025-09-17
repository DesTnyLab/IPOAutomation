# # app/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import CompanyShare



from celery import shared_task


@shared_task
def delete_expired_sheres():
    now = timezone.now()
    
    # Get all expired shares (<= current time)
    expired = CompanyShare.objects.filter(issue_close_date__lte=now)
    
    # Count them before deleting
    count = expired.count()
    
    # Delete the expired records
    expired.delete()
    
    return f"Deleted {count} expired shares."


