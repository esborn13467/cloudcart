from django.urls import path
from . import views

app_name = 'userauths'

urlpatterns = [
    # path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.loggin, name='login'),
    # path('logout_view', views.logout_view, name='logout_view'),
]