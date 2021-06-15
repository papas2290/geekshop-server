from django.urls import path
from adminapp.views import index , UserListView, UserCreateView, UserUpdateView, UserDeleteView
app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin_users_read/', UserListView.as_view(), name='admin_users_read'),
    path('admin_users_create/', UserCreateView.as_view(), name='admin_users_create'),
    path('admin_users_update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('admin_users_remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
]
