from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def today(request):
    return render(request, 'main/today.html')

def tomorrow(request):
    return render(request, 'main/tomorrow.html')