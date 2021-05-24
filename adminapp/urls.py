from django.urls import path
from adminapp.views import index, admin_users_read, admin_users_create

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin_users_read/', admin_users_read, name='admin_users_read'),
    path('admin_users_create/', admin_users_create, name='admin_users_create'),
]
