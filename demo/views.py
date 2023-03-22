import datetime
#пишутся обработчики запросов
from django.shortcuts import render
from django.http import HttpResponse, Http404
from demo.models import Product
# Create your views here.

def index(request):
    return HttpResponse('you can see it')

def time(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'demo/list.html', {'products': products})

def product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'demo/details.html', {'prod': product})
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

