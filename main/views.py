from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Store - Главная',
        'content': "",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Store - О нас',
        'content': "О нас",
        'text_on_page': "Store is cool."
    }

    return render(request, 'main/about.html', context)