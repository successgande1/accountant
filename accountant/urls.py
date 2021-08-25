"""accountant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cashier import views as cashier_view
from django.contrib.auth import views as auth_view
from dashboard import views as dashbaord_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', cashier_view.register, name = 'user-add'),
    path('profile/', cashier_view.profile, name = 'user-profile'),
    path('expenses/', cashier_view.AddExpenses, name = 'user-add-expenses'),
    path('income/', cashier_view.AddIncome, name = 'user-add-income'),
    path('expenses/list/', cashier_view.list_Expense, name = 'user-list-expenses'),
    path('income/list/', cashier_view.list_Income, name = 'user-list-income'),
    path('income/monthly/list/', cashier_view.monthly_Income, name = 'user-list-monthly-income'),
    path('profile/update/', cashier_view.profile_update, name = 'user-profile-update'),
    path('income/delete/', dashbaord_view.user_income_delete, name = 'income-delete'),
    path('', auth_view.LoginView.as_view(template_name='cashier/login.html'), name = 'cashier-login'),
     path('logout/', auth_view.LogoutView.as_view(template_name='cashier/logout.html'), name = 'cashier-logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
