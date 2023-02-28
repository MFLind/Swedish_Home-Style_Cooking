from django.urls import path
from swebooking import views


urlpatterns = [
    path('', views.home, name='home'),
]
