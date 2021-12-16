from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


def auth(request):
    if request.user.is_authenticated:
        # do something
        print(request.user)
        return render(request, 'registration.html')
    else:
        print(request.user)
        return render(request, 'registration.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(username=email)
            user = authenticate(request, username=email, password=password,
                                email=email)
            if user is not None:
                dj_login(request, user)
                # messages.success(request, 'You are logged in.')
                return redirect("CHECK")
            else:
                return render(request, "registration.html", {"error": "Invalid email or password"})
        except User.DoesNotExist:

            return render(request, "registration.html", {"error": "No user associated with this email"})


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=email, email=email, password=password, first_name=fname,
                                            last_name=lname)
            user.save()
            dj_login(request, user)
            return redirect('CHECK')
        except IntegrityError:
            return render(request, 'registration.html', {'error': 'User with this email already exists.'})


def logout(request):
    print(request.user)
    dj_logout(request)
    return redirect("MAIN")
