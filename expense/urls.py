"""contractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    # Project URLS
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('project/add/', views.ProjectCreate.as_view(), name='project-add'),
    path('project/<int:pk>/', views.ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    # Category URLs
    path('categories/', views.CategoryCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
    # Expense URLs
    path('expenses/', views.ExpenseList.as_view(), name='expense-list'),
    path('expenses/add/', views.ExpenseCreate.as_view(), name='expense-add'),
    path('expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expense-update'),
    path('expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense-delete'),
    # Cost Limit URLs
    path('costlimits/', views.CostLimitList.as_view(), name='costlimit-list'),
    path('costlimits/add/', views.CostLimitCreate.as_view(), name='costlimit-add'),
    path('costlimits/<int:pk>/update/', views.CostLimitUpdate.as_view(), name='costlimit-update'),
    path('costlimits/<int:pk>/delete/', views.CostLimitDelete.as_view(), name='costlimit-delete'),
    # Payee URLs
    path('payees/', views.PayeeList.as_view(), name='payee-list'),
    path('payees/add/', views.PayeeCreate.as_view(), name='payee-add'),
    path('payees/<int:pk>/update/', views.PayeeUpdate.as_view(), name='payee-update'),
    path('payees/<int:pk>/delete/', views.PayeeDelete.as_view(), name='payee-delete'),
]
