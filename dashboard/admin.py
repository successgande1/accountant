from django.contrib import admin

from .models import Expenditure, Income

from django.contrib.auth.models import Group

#Customise the Admin Header
admin.site.site_header = 'SUCCESS ICT Accountant'

#Customize The Display of Model in a Table inside the Admin Pannel
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'staff', 'amount', 'date', 'addedDate')

# Register your models here and also pass your class Admin for List Display if available.
admin.site.register(Expenditure, ExpenditureAdmin)

admin.site.register(Income)