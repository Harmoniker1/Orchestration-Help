"""
Definition of urls for Orchestration_Help.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path("", views.home, name = "home"),
    path("contact/", views.contact, name = "contact"),
    path("about/", views.about, name = "about"),
    path("instruments/", views.instruments, name = "instruments"),
    path("instruments/<str:instrument>/", views.specific_instrument, name = "specific_instrument"),
    path("admin/", admin.site.urls),
]