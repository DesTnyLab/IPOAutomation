from django.db import models


class CompanyShare(models.Model):
    company_share_id = models.PositiveIntegerField(unique=True)  # from API (companyShareId)
    scrip = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255)
    share_type_name = models.CharField(max_length=50)
    share_group_name = models.CharField(max_length=100)
    sub_group = models.CharField(max_length=100)
    status_name = models.CharField(max_length=50)
    issue_open_date = models.DateTimeField()
    issue_close_date = models.DateTimeField()


    def __str__(self):
        return f"{self.company_name} ({self.scrip})"


