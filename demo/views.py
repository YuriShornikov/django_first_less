import datetime
#пишутся обработчики запросов
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('you can see it')

def time(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')

