from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products."""

    products = Product.objects.all()

    context = {
        'prdoucts': products,
    }

    return render(request, 'product/products.html', context)
