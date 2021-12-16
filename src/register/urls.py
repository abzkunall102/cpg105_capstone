from django.urls import path

from .views import *

urlpatterns = [
    path('', auth, name='AUTH_PAGE'),
    path('register/', register, name='REGISTER'),
    path('login', login, name='LOGIN'),
    path('logout', logout, name='LOGOUT')
]
