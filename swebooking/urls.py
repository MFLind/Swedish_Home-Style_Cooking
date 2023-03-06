"""
Swebooking URLs
"""
from django.contrib.auth.decorators import login_required
from django.urls import path
from swebooking import views
from .views import SignUpView


urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('booking/', login_required(views.BookingView.as_view()), name='booking'),
    path('seebookings/', views.seebookings, name='seebookings'),
    path('edit/<int:booking_id>', login_required(views.EditView.as_view()), name='edit'),
    path('delete/<int:booking_id>', login_required(views.DeleteView.as_view()), name='delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
