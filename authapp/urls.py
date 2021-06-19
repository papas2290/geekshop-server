from django.urls import path

from authapp.views import verify
# import authapp.views
from authapp.views import profile ,logout
from authapp.views import Login
from authapp.views import register
app_name = 'auth'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('verify/<email>/<key>/', verify, name='verify'),
    ]
