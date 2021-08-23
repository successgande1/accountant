from django.urls import path

from . import views
from cashier import views as user_view

urlpatterns = [
    path('dashboard/', views.index, name = 'dashboard-index'),
]