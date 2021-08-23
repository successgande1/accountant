from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_INCOME = (
    ('Printing / Photostart / Printing', 'Printing / Photostart / Printing'),
    ('Typing ', 'Typing'),
    ('Graphic Design / Passport', 'Graphic Design / Passport'),
    ('Email Creation / Checking', 'Email Creation / Checking'),
    ('Online Application', 'Online Application'),
    ('Result', 'Result'),
    ('Computer Training Fee', 'Computer Training Fee'),
    ('Laminating', 'Laminating'),
    ('Sell of Agreement Form', 'Sale of Agreement Form'),
    ('Sell of Envelope / Binding Film', 'Sell of Envelope / Binding Film'),
)

CATEGORY_EXPENSES = (
    ('Stationaries', 'Stationaries'),
    ('Family Up Keep', 'Family Up Keep'),
    ('Airtime Recharge', 'Airtime Recharge'),
    ('Fittings / Repairs', 'Fittings / Repairs'),
    ('Staff Salary', 'Staff Salary'),
    ('Generator Maintainance', 'Generator Maintainance'),
)

class Expenditure(models.Model):  
    description = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, choices=CATEGORY_EXPENSES, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(null=False)
    Remarks = models.CharField(max_length=120, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False, null=False)
    addedDate = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        verbose_name_plural = 'Expenses'

    def __str__(self):
        return self.description

class Income(models.Model): 
    description = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, choices=CATEGORY_INCOME, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(null=False)
    remarks = models.CharField(max_length=120, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False, null=False)
    addedDate = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = 'Income Sources'

    def __str__(self):
        return self.description
