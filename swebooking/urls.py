from django.urls import path
from swebooking import views
from .views import SignUpView


urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('seebookings/', views.seebookings, name='seebookings'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
