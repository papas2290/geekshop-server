from django.shortcuts import render
from mainapp.models import Product, ProductCategory
# Create your views here.


def index(request):
    context = {
        'title': 'главная страница',
        'date': 'It is '
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Страница товаров',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html',  context)
