from itertools import product

from django.shortcuts import render
from django.template.context_processors import request

from core.models import Product, Category


# Create your views here.
def index(request):
    product = Product.objects.all().order_by("-date")
    featured_product = Product.objects.filter(product_status="published", featured=True).order_by("-date")

    context = {
        'products': product,
        'featured_products': featured_product,
    }

    return render(request, 'index.html', context)


def category(request, title):
    category = Category.objects.get(title=title)
    product = Product.objects.filter(category=category).order_by("-date")

    context = {
        'category': category,
        'products': product,
        'breadcrumb_title': title
    }

    return render(request, 'category.html', context)


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
    product = Product.objects.all().order_by("-date")
    context = {
        'all_products':product,
        'breadcrumb_title': 'Shop'
    }
    return render(request, 'shop-grid.html', context)


def shoping_cart(request):
    context = {
        'breadcrumb_title': 'Shoping Cart'
    }
    return render(request, 'shoping-cart.html', context)
