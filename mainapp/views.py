from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'Страница товаров',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.0},
            {'name': 'Синяя куртка The North Face', 'price': 23725.0},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.0},
            {'name': 'Черный рюкзак Nike Heritage', 'price': 2340.0},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.0},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': 2890.0},

        ]
    }
    return render(request, 'mainapp/products.html', context)
