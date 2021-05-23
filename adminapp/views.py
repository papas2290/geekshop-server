from django.shortcuts import render
from authapp.models import User

def index(request):
    return render(request, 'adminapp/admin.html')


def admin_users_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin_users_read.html', context)
