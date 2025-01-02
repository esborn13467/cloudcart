from core.models import Category, Address
from django.core.exceptions import ObjectDoesNotExist

def global_info(request):
    categories = Category.objects.all()
    address = None
    try:
        address = Address.objects.get(user=request.user)
    except ObjectDoesNotExist:
        pass
    return {
        'global_categories': categories,
        'address': address
    }