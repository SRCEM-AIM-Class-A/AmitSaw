from django.urls import path
from .views import index, contact, services

urlpatterns = [
    path('', index, name='app2_index'),  # This handles /app2/
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
]
