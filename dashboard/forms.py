from django import forms
from .models import Expenditure, Income

#Date Picket Widgets for date field in Income and Expenditure
class IncomeDateField(forms.DateInput):
    input_type = 'date'


#Add Expenditure Form
class ExpensesForm(forms.ModelForm):
    class Meta:
        widgets = {'date':IncomeDateField()}
        model = Expenditure
        fields = ['date', 'description', 'category', 'amount', 'Remarks']

#Add Income Form
class IncomeForm(forms.ModelForm):
    class Meta:
        widgets = {'date':IncomeDateField()}
        model = Income
        fields = ['date', 'description', 'category', 'amount', 'remarks']

class ExpenseUpdate(forms.ModelForm):
    class Meta:
        widgets = {'date':IncomeDateField()}
        model = Expenditure
        fields = ['date', 'description', 'category', 'amount', 'Remarks']

class IncomeUpdate(forms.ModelForm):
    class Meta:
        widgets = {'date':IncomeDateField()}
        model = Income
        fields = ['date', 'description', 'category', 'amount', 'remarks']

class IncomeSearchForm(forms.ModelForm):
    start_date = forms.DateField(required=True, widget = IncomeDateField)
    end_date = forms.DateField(required=True, widget = IncomeDateField)
    class Meta:
        model = Income
        fields = [ 'description', 'start_date', 'end_date']