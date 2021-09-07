from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from dashboard .forms import ExpensesForm, IncomeForm, IncomeUpdate, ExpenseUpdate, IncomeSearchForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dashboard.models import Expenditure, Income
from django.db.models.functions import TruncMonth
from django.db.models import Count, Sum
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.
@login_required(login_url='cashier-login')
def login(request):
    return render(request, 'user/login.html')

#Add New User Method
@login_required(login_url='cashier-login')
def register(request):
    #Create variable and query all users
    workers = User.objects.all()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Added Successfully')
            return redirect('user-add')
    else:
        form = CreateUserForm()
    context = {
        'form':form,
        'workers':workers,
    }
    return render(request, 'dashboard/user_register.html', context)

#View Profile method
@login_required(login_url='cashier-login')
def profile(request):
    return render(request, 'cashier/profile.html')

#Update Profile Method
@login_required(login_url='cashier-login')
def profile_update(request):
    if request.method == 'POST':
        #create user form variable
        user_form = UserUpdateForm(request.POST, instance=request.user)
        #create update form variable
        profile_form = ProfileUpdateForm(request.POST, request.FILES, 
        instance=request.user.profile)
    #Check if both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile Updated Successfully')
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'cashier/profile_update.html', context)

#Add Expenses Method
@login_required(login_url='cashier-login')
def AddExpenses(request):
    if request.method == 'POST':
        Add_expense_form = ExpensesForm(request.POST)
        if Add_expense_form.is_valid():
            Add_expense_form.save()
            expense_name = Add_expense_form.cleaned_data['description']
            expense_date = Add_expense_form.cleaned_data['date']
            messages.success(request, f'{expense_name} Expenditure Item for {expense_date} Added Successfully')
            return redirect('user-list-expenses')
    else:
        Add_expense_form = ExpensesForm()
    context = {
        'Add_expense_form':Add_expense_form,
    }
    return render(request, 'cashier/add_expenses.html', context)

#Add Income Method
@login_required(login_url='cashier-login')
def AddIncome(request):
    if request.method == 'POST':
        Add_income_form = IncomeForm(request.POST)
        if Add_income_form.is_valid():
            Add_income_form.save()
            #Get Description field name from Income Form
            income_name = Add_income_form.cleaned_data['description']
            income_date = Add_income_form.cleaned_data['date']
            messages.success(request, f'{income_name} Income for {income_date} Added Successfully')
            return redirect('user-list-income')
    else:
        Add_income_form = IncomeForm()
    context = {
        'Add_income_form':Add_income_form,
    }
    return render(request, 'cashier/add_income.html', context)

#Method for Updating Income Income Item
@login_required(login_url='cashier-login')
def UpdateIncome(request, pk):
    income_item = Income.objects.get(id=pk)
    if request.method == "POST":
        income_update_form = IncomeUpdate(request.POST, instance=income_item)
        if income_update_form.is_valid():
            income_update_form.save()
            messages.success(request, f'{income_item} information Updated Successfully')
            return redirect('user-list-income')
    else:
        income_update_form = IncomeUpdate(instance=income_item)
    context = {
        'income_update_form':income_update_form,
        'income_item':income_item,
    }
    return render(request, 'cashier/income_update.html', context)

#Method for Updating Expenditure Item
@login_required(login_url='cashier-login')
def Updateexpense(request, pk):
    expense_item = Expenditure.objects.get(id=pk)
    if request.method == "POST":
        expense_update_form = ExpenseUpdate(request.POST, instance=expense_item)
        if expense_update_form.is_valid():
            expense_update_form.save()
            messages.success(request, f'{expense_item} information Updated Successfully')
            return redirect('user-list-expenses')
    else:
        expense_update_form = ExpenseUpdate(instance=expense_item)
    context = {
        'expense_update_form':expense_update_form,
        'expense_item':expense_item,
    }
    return render(request, 'cashier/expense_update.html', context)

#List Expenses method
@login_required(login_url='cashier-login')
def list_Expense(request):
    #Query Expenditure List
    list_expenses = Expenditure.objects.order_by('-date')

    paginator = Paginator(list_expenses, 5)
    page = request.GET.get('page')
    paged_expenses = paginator.get_page(page)

    context = {
        'list_expenses':paged_expenses
    }

    return render(request, 'cashier/list_expenses.html', context)

#List Income method
@login_required(login_url='cashier-login')
def list_Income(request):
    #Query Income List
    list_income = Income.objects.order_by('-date')

    paginator = Paginator(list_income, 5)
    page = request.GET.get('page')
    paged_income = paginator.get_page(page)

     #Get Day of today from current date and time
    #now = datetime.datetime.now()
    #Query Total Income for current Month in the current Year
    #monthly_total = Income.objects.filter(date__year=now.year, date__month=now.month).aggregate(monthly_total=Sum('amount'))['monthly_total']

    context = {
        'list_income':paged_income,
    }

    return render(request, 'cashier/list_income.html', context)

#Income Search Date Range Method
@login_required(login_url='cashier-login')
def SearchIncomeRange(request):
    listIncome = Income.objects.all()
    searchForm = IncomeSearchForm(request.POST or None)
  
    
    if request.method == 'POST':
        listIncome = Income.objects.filter(date__range=[searchForm['start_date'].value(),
                                searchForm['end_date'].value()
                            ]
        )
        
    else:
        searchForm = IncomeSearchForm()

    #listIncome = listIncome 
    paginator = Paginator(listIncome, 5)
    page = request.GET.get('page')
    paged_listIncome = paginator.get_page(page)
    
    #Calculate total amount of Date Range Result
    total = listIncome.aggregate(total = Sum('amount')).get('total') or 0

    context = {
        'listIncome':paged_listIncome,
        'searchForm':searchForm,
        'total':total,
    }
    
    return render(request, 'cashier/search_income_range.html', context)


#View Monthly Income method
@login_required(login_url='cashier-login')
def monthly_Income(request):

    #Get Day of today from current date and time
    now = datetime.datetime.now()
    total_income = Income.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('amount'))

    context = {
        'total_income': total_income,
    }       
    return render(request, 'cashier/view_income_monthly.html', context)

#View Monthly Income method
@login_required(login_url='cashier-login')
def monthly_Expenses(request):

    #Get Day of today from current date and time
    now = datetime.datetime.now()
    total_expenses = Expenditure.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_amount=Sum('amount'))

    context = {
        'total_expenses': total_expenses,
    }       
    return render(request, 'cashier/view_expenses_monthly.html', context)

#View Monthly Gross Profit, Expenditure, and Net Income method
@login_required(login_url='cashier-login')
def monthly_yearly_Income(request):

    #Get Day of today from current date and time
    now = datetime.datetime.now()

    total_monthly_income = Income.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_monthly_income=Sum('amount'))
    total_monthly_expenses = Expenditure.objects.annotate(month=TruncMonth('date')).values('month').annotate(total_monthly_expenses=Sum('amount'))
    income_expense = zip(total_monthly_income, total_monthly_expenses)
    
    net_monthly_income_list = []
    
    for income, expense in income_expense:
        net_monthly_income_list.append(income.get('total_monthly_income', 0) - expense.get('total_monthly_expenses', 0)) or 0
    
    income_list = zip(total_monthly_income, total_monthly_expenses, net_monthly_income_list)
    
    context = {
        'income_list': income_list
    }

    return render(request, 'cashier/monthly_yearly_income_expense.html', context)