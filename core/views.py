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
    return render(request, 'checkout.html')


def contact(request):
    return render(request, 'contact.html')


def shop_details(request):
    return render(request, 'shop-details.html')


def shop_grid(request):
    return render(request, 'shop-grid.html')


def shoping_cart(request):
    return render(request, 'shoping-cart.html')
