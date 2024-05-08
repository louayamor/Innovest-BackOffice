"""
URL configuration for Innovest_BackOffice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home import views

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dashboard.html')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('users', views.users, name='users'),
    path('businesses', views.businesses, name='businesses'),
    path('investments', views.investments, name='investments'),
    path('sectors', views.sectors, name='sectors'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('add_admin/', views.add_admin, name='add_admin'),
    path('authentication-login/', views.LoginView.as_view(), name='authentication-login'),
]