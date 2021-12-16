from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='MAIN'),
    path('contact', contact, name='CONTACT'),
    path('check/', upload, name='CHECK')
]
