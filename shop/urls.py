from django.urls import path
from .models import *
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', product_list, name="product_list"),
    path('<int:id>/<str:slug>/detail/', product_detail, name="product_detail"),
]
