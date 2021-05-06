from django.shortcuts import render

def login(request):
    context = {'title': 'Geekshop- Авторизация' }
    return render(request, 'authapp/login.html', context)
