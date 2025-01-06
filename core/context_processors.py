from core.models import Category, Address
from django.core.exceptions import ObjectDoesNotExist

def global_info(request):
    categories = Category.objects.all()
    address = None
    try:
        if request.user.is_authenticated:
            address = Address.objects.get(user=request.user.id)
    except ObjectDoesNotExist:
        address = None
    return {
        'global_categories': categories,
        'address': address
    }