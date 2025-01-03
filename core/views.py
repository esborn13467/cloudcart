from itertools import product

from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request

from core.models import Product, Category, Vendor


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
    product = Product.objects.filter(category=category, product_status="published").order_by("-date")

    context = {
        'category': category,
        'products': product,
        'breadcrumb_title': title,
        'breadcrumb_subtitle': "Categories/" + title
    }

    return render(request, 'category.html', context)


def category_list(request):
    context = {
        'breadcrumb_title': "Categories",
        'breadcrumb_subtitle': "Categories"
    }

    return render(request, 'categories.html', context)


def vendor_list(request):
    vendor = Vendor.objects.all()
    context = {
        'vendors': vendor,
        'breadcrumb_title': "Vendor List",
        'breadcrumb_subtitle': "Vendor List"
    }

    return render(request, 'vendor-list.html', context)


def vendor_details(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")
    context = {
        'vendor': vendor,
        'products': products,
        'breadcrumb_title': "Vendor Details",
        'breadcrumb_subtitle': "Vendors - " + vendor.title
    }
    return render(request, 'vendor-details.html', context)
    
    
def checkout(request):
    context = {
        'breadcrumb_title': 'Checkout',
        'breadcrumb_subtitle': 'Checkout'
    }
    return render(request, 'checkout.html', context)


def contact(request):
    context = {
        'breadcrumb_title': 'Contact',
        'breadcrumb_subtitle': 'Contact'
    }
    return render(request, 'contact.html', context)


def product_details(request, pid):
    product = Product.objects.get(pid=pid)
    # products = get_object_or_404(Product, pid=pid)
    product_image = product.product_images.all()
    context = {
        'product': product,
        'product_images': product_image,
        'breadcrumb_title': 'Product-details',
        'breadcrumb_subtitle': 'Products/' + product.title
    }
    return render(request, 'product-details.html', context)


def product_list(request):
    product = Product.objects.all().order_by("-date")
    context = {
        'all_products': product,
        'breadcrumb_title': 'All Products',
        'breadcrumb_subtitle': 'All Products'
    }
    return render(request, 'product-list.html', context)


def shoping_cart(request):
    context = {
        'breadcrumb_title': 'Shoping Cart',
        'breadcrumb_subtitle': 'Shoping Cart'

    }
    return render(request, 'shoping-cart.html', context)
