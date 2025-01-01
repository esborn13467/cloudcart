from django.contrib import admin
from core.models import Category, Vendor, Product, ProductImages, CartOrder, CartOrderItems, ProductReview, Wishlist, \
    Address


# Register your models here.
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['product', 'product_image']
    list_filter = ['product']
    search_fields = ['product__title']



class ProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'product_image', 'category', 'price','vendor', 'featured', 'product_status']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']


class CartOderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'paid_status', 'order_date', 'product_status']


class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_number', 'item', 'image', 'quantity', 'price', 'total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
