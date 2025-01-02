from core.models import Category, Product


def global_categories(request):
    categories = Category.objects.all()
    return {'global_categories': categories}

def global_products(request):
    products = Product.objects.all()
    return {'global_products': products}