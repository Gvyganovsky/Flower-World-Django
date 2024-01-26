from django.shortcuts import render

from flowershop.models import Product


def index(request):
    product = Product.objects.filter(counts__gt=0)
    return render(request, 'index.html', context={'product': product})
