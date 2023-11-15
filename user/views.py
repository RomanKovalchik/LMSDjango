from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.


def index(request: WSGIRequest):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'user/index.html', context=context)

