from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug__iexact=category_slug)
        products = Product.objects.filter(category=category)
    context = {"products" : products, "categories": categories, "category":category}
    return render(request, "shop/product/list.html", context)

def product_detail(request, slug, id):
    product = Product.objects.get(slug__iexact=slug)
    context = {"product" : product}
    return render(request, "shop/product/detail.html", context)
