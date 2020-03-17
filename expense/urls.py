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
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('project/add/', views.ProjectCreate.as_view(), name='project-add'),
    path('project/<int:pk>/', views.ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    # Category URLs
    path('categories/', views.CategoryCreate.as_view(), name='category-list'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
    # Expense URLs
    # path('expenses/', views.ProjectListView.as_view(), name='project_list'),
    # path('expenses/add/', views.ProjectCreate.as_view(), name='project-add'),
    # path('expenses/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project-update'),
    # path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
]
