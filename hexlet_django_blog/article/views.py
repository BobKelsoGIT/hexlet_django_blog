from django.shortcuts import render
from django.conf import settings


def index(request):
    context = {
        'app_name': settings.APP_NAME,
    }
    return render(request, 'articles/index.html', context)
