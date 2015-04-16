from django.shortcuts import render


def home_view(request, template='main/home.html'):
    return render(request, template)