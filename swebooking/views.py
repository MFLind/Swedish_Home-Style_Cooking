from django.shortcuts import render


def home(request):
    return render(request, 'swebooking/index.html')


def menu(request):
    return render(request, 'swebooking/menu.html')


def booking(request):
    return render(request, 'swebooking/booking.html')

