from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_INCOME = (
    ('Document Printing/Photostart ', 'Document Printing/Photostart'),
    ('Document Typing / Printing ', 'Document Typing / Printing'),
    ('Document Scan / Emailing ', 'Document Scan / Emailing'),
    ('Website / Software Development ', 'Website / Software Development'),
    ('Document Colored Print ', 'Document Colored Print'),
    ('Graphic Design', 'Graphic Design'),
    ('Email Creation / Checking ', 'Email Creation / Checking'),
    ('Online Application / Registration', 'Online Application / Registration'),
    ('Result Check', 'Result Check'),
    ('Computer Training Fee', 'Computer Training Fee'),
    ('Document Laminating', ' Document Laminating'),
    ('Sale of Agreement Form', 'Sale of Agreement Form'),
    ('Sale of Envelope / Binding Film', 'Sale of Envelope / Binding Film'),
)

CATEGORY_EXPENSES = (
    ('Stationaries', 'Stationaries'),
    ('Family Up Keep', 'Family Up Keep'),
    ('Airtime Recharge', 'Airtime Recharge'),
    ('Fittings / Repairs', 'Fittings / Repairs'),
    ('Staff Salary', 'Staff Salary'),
    ('Generator / Bike Maintainance', 'Generator / Bike Maintainance'),
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
