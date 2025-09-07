from django.db import models
from django.forms import ValidationError
import random


class AccountDetailsManager(models.Manager):
    def random(self):
        count = self.count()
        if count == 0:
            return None
        random_index = random.randint(0, count - 1)
        return self.all()[random_index]

class AccountDetials(models.Model):
    name = models.CharField(max_length=100)
    dp_id = models.CharField(max_length=20)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    crn_number = models.CharField(max_length=20, unique=True)
    pin = models.CharField(max_length=10)
    clientId = models.CharField(max_length=100, blank=True, null=True)

    objects = AccountDetailsManager()
    
    @property
    def get_boid(self):
        return self.username
    
    @property
    def get_demat(self):
        return f'130{self.dp_id}{self.username}'

    def __str__(self):
        return self.name
    
    def clean(self):
        """
        Automatically fill or validate clientId from DpIdReverse
        """
        if self.dp_id:
            try:
                mapping = DpIdReverse.objects.get(dp_id=self.dp_id)
                if not self.clientId or self.clientId != mapping.clientId:
                    self.clientId = mapping.clientId
            except DpIdReverse.DoesNotExist:
                raise ValidationError({"dp_id": "No matching dp_id found in DpIdReverse."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    



class BankDetails(models.Model):
    account = models.ForeignKey(AccountDetials, on_delete=models.CASCADE, related_name="bankdetails")
    customer_id = models.CharField(max_length=10, unique=True)
    account_number = models.CharField(max_length=20, unique=True)
    account_type_id = models.CharField(max_length=5)
    bank_id = models.CharField(max_length=5)
    account_branch_id = models.CharField(max_length=10)


    def __str__(self):
        return self.account_number
    




    


class DpIdReverse(models.Model):
    dp_id = models.CharField(max_length=20, unique=True)
    clientId = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)

    def get_clientId(self):
        return self.clientId
    
    def __str__(self):
        return f"{self.name} - {self.dp_id}"
