from django.contrib.auth import authenticate, login, logout
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from user.forms import CustomUserCreationForm, CustomUserLoginForm


# Create your views here.


def index(request: WSGIRequest):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'user/index.html', context=context)


def register_view(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('course_index')

    return render(request, 'user/register.html', {'form': form})


def login_view(request):
    form = CustomUserLoginForm(request.POST)

    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('course_index')

    return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

