from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    # Тренировка
    # path('login/', user_login, name = 'user_login'),
    path('', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
