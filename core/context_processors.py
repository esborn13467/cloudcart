from core.models import Category


def global_categories(request):
    categories = Category.objects.all()
    return {'global_categories': categories}
