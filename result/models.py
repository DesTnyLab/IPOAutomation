from django.db import models

from account.models import AccountDetials
# Create your models here.


class Report(models.Model):
    user = models.ForeignKey(AccountDetials, on_delete=models.CASCADE)
    scrip = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    share_type_name = models.CharField(max_length=50)
    share_group_name = models.CharField(max_length=100)
    applicant_form_id = models.PositiveIntegerField()  # from API
  
    def __str__(self):
        return f"Report for {self.user.username} - {self.company_name}"
    


