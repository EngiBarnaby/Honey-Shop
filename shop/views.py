from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {"products" : products, "categories": categories}
    return render(request, "shop/product/list.html", context)

def product_detail(request, slug, id):
    product = Product.objects.get(slug__iexact=slug)
    context = {"product" : product}
    return render(request, "shop/product/detail.html", context)
