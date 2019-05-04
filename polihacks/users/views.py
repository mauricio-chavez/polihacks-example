from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_dj


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login_dj(request, user)
            return redirect('welcome')
        else:
            return render(request, 'users/login.html', {'error': 'Inicia sesión'})
    else:
        return render(request, 'users/login.html')