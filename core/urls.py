from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    path('product/<str:pid>', views.product_details, name='product-details'),
    path('products/', views.product_list, name='product-list'),

    # Category
    path('category/<str:title>/', views.category, name='category'),
    path('categories/', views.category_list, name='categories'),

    # Vendor
    path('vendors/', views.vendor_list, name='vendor-list'),
    path('vendor/<str:vid>/', views.vendor_details, name='vendor-details'),

    path('products/tag/<slug:tag_slug>/', views.tag_list, name='tag-list'),

    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shoping-cart/', views.shoping_cart, name='shoping-cart'),


    ]