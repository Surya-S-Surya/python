from django.urls import path
from . import views

urlpatterns = [
    path('book_ticket/', views.book_ticket, name='book_ticket'),
    # Add other paths as needed
]
