from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Expenditure, Income
#from .forms import ProductForm, SalesForm
from django.contrib.auth.models import User
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum
from django.db import connection
from datetime import datetime
import datetime


from django.contrib import messages

# List Staff and expenses, income by Current month Method
@login_required(login_url='cashier-login')
def index(request):

    #List workers
    workers = User.objects.all()

    #List Only 2 Expenditures
    expenses = Expenditure.objects.order_by('-date')[:2]

    #List Only 2 Incomes
    income = Income.objects.order_by('-date')[:3] 

    #List All the Incomes
    all_income = Income.objects.order_by('-date')[:5]

    #Get Day of today from current date and time
    now = datetime.datetime.now()

    date_today = datetime.datetime.now().date

    #Query Total Income for current Month in the current Year
    total_income = Income.objects.filter(date__year=now.year, date__month=now.month).aggregate(total_income=Sum('amount')).get('total_income') or 0

    

    #Query Expenditure for Total Current Monthly Expenses
    total_monthly_expenses = Expenditure.objects.filter(date__year=now.year, date__month=now.month).aggregate(total_monthly_expenses=Sum('amount')).get('total_monthly_expenses') or 0

    #Query Daily Income of the month
    daily_income = Income.objects.filter(date__year=now.year, date__month=now.month, date__day=now.day).aggregate(daily_income=Sum('amount')).get('daily_income') or 0

    
    #Calculation of Total Income and Expenditure difference
    net_monthly_income = total_income - total_monthly_expenses

    context = {
        'workers':workers,
        'expenses':expenses,
        'income':income,
        'total_income':total_income,
        'year': now.year,
        'month': now.month,
        'date_today': date_today,
        'total_monthly_expenses' : total_monthly_expenses,
        'net_monthly_income' : net_monthly_income,
        'daily_income': daily_income,
        'all_income':all_income,
        
    }
    return render(request, 'dashboard/index.html', context)