from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html')

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    return render(request, 'app1/contact.html')  # Ensure 'contact.html' exists

def services(request):
    return render(request, 'app1/services.html')  # Ensure 'services.html' exists
