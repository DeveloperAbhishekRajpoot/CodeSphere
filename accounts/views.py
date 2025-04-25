from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# SIGNUP VIEW
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'signUp.html', {'error': 'Email already in use'})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signUp.html', {'error': 'Username already taken'})

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('explore')  # change this to your actual home page

    return render(request, 'signUp.html')


# LOGIN VIEW (using email)
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('explore')  # change this to your actual home page
            else:
                return render(request, 'signUp.html', {'login_error': 'Invalid email or password'})
        except User.DoesNotExist:
            return render(request, 'signUp.html', {'login_error': 'Invalid email or password'})

    return render(request, 'signUp.html')


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect('login')  # or send them to landing/login page
