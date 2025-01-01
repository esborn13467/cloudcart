from django.shortcuts import render
from django.template.context_processors import request

from core.models import Product, Category


# Create your views here.
def index(request):
    product = Product.objects.all().order_by("-date")
    featured_product = Product.objects.filter(product_status="published", featured=True).order_by("-date")
    category = Category.objects.all()

    context = {
        'all_products': product,
        'featured_products': featured_product,
        'categories': category
    }

    return render(request, 'index.html', context)


def checkout(request):
    context = {
        'breadcrumb_title': 'Checkout'
    }
    return render(request, 'checkout.html', context)


def contact(request):
    context = {
        'breadcrumb_title': 'Contact'
    }
    return render(request, 'contact.html', context)


def shop_details(request):
    context = {
        'breadcrumb_title': 'Shop-details'
    }
    return render(request, 'shop-details.html', context)


def shop_grid(request):
    context = {
        'breadcrumb_title': 'Shop'
    }
    return render(request, 'shop-grid.html', context)


def shoping_cart(request):
    context = {
        'breadcrumb_title': 'Shoping Cart'
    }
    return render(request, 'shoping-cart.html', context)
