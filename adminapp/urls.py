from django.urls import path
from adminapp.views import index, admin_users_read

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin_users_read', admin_users_read, name='admin_users_read'),
]
