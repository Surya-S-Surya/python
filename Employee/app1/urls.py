from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('search/', views.search_employee, name='search_employee'),
    # Add more URL patterns if needed
]
