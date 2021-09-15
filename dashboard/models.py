from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_INCOME = (
    ('Photostart ', 'Photostart'),
    ('Typing / Printing ', 'Typing / Printing'),
    ('Scan / Emailing ', 'Scan / Emailing'),
    ('Web Development ', 'Web Development'),
    ('Colored Print ', 'Colored Print'),
    ('Graphic Design', 'Graphic Design'),
    ('Email ', 'Email Creation / Checking'),
    ('Online Registration', 'Online Registration'),
    ('Result Check', 'Result Check'),
    ('Training Fee', 'Training Fee'),
    ('Lamination', ' Lamination'),
    ('Agreement Form', 'Agreement Form'),
    ('Envelope / Binding Film', 'Envelope / Binding Film'),
)

CATEGORY_EXPENSES = (
    ('Income', 'Income'),
    ('Saving', 'Saving'),
    ('Debt', 'Debt'),
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
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.PositiveIntegerField(null=False)
    remarks = models.CharField(max_length=120, null=True)
    date = models.DateField(auto_now_add=False, auto_now=False, null=False)
    addedDate = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name_plural = 'Income Sources'

    def __str__(self):
        return self.description
