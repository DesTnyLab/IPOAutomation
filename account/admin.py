from django.contrib import admin

from .models import AccountDetials, BankDetails, DpIdReverse
# Register your models here.


admin.site.register(AccountDetials)
admin.site.register(BankDetails)
admin.site.register(DpIdReverse)
