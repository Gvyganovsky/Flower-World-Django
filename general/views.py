from django.shortcuts import render

from flowershop.models import Product


def index(request):
    product = Product.objects.filter(counts__gt=0)
    return render(request, 'index.html', context={'product': product})


def product_page(request, product_id):
    product = Product.objects.get(id=product_id)

    return  render(request, 'product.html', context={'product': product})


def login(request):
    return render(request, 'login.html', context={'login': login})