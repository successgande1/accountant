from django import forms
from .models import Expenditure, Income

#Add Expenditure Form
class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['description', 'category', 'amount', 'Remarks', 'date']

#Add Income Form
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['description', 'category', 'amount', 'remarks', 'date']