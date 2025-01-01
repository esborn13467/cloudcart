from django.shortcuts import render

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


def electronic(request):
    return render(request, 'electronic.html')


def fashion(request):
    return render(request, 'fashion.html')
