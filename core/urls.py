from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('shop-details/', views.shop_details, name='shop-details'),
    path('shop-grid/', views.shop_grid, name='shop-grid'),
    path('shoping-cart/', views.shoping_cart, name='shoping-cart'),
    path('category/<str:title>/', views.category, name='category'),
    path('categories/', views.category_list, name='categories'),
    path('vendors/', views.vendor_list, name='vendor-list'),
    path('vendor/<str:vid>/', views.vendor_details, name='vendor-details'),

    ]