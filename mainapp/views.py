from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.


def index(request):
    context = {
        'title': 'главная страница',
        'date': 'It is '
    }
    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None):
    context = {'title': 'Geek Shop каталог', 'categories': ProductCategory.objects.all()}
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        context.update({'products': products})
    else:
        context.update({'products': Product.objects.all()})
    return render(request, 'mainapp/products.html',  context)
