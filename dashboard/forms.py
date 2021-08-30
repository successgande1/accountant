from django import forms
from .models import Expenditure, Income

#Add Expenditure Form
class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['date', 'description', 'category', 'amount', 'Remarks']

#Add Income Form
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'description', 'category', 'amount', 'remarks']

class ExpenseUpdate(forms.ModelForm):
    class Meta:
        model = Expenditure
        fields = ['date', 'description', 'category', 'amount', 'Remarks']

class IncomeUpdate(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['date', 'description', 'category', 'amount', 'remarks']