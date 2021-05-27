from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminPrifileForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin_users_read.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin_users_create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admin_staff:admin_users_read')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin_users_update_delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
    form_class = UserAdminPrifileForm


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin_users_update_delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
