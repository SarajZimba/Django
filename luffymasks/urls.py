from django.urls import path
from . import views

urlpatterns = [
   # path('', views.home, name = 'home'),
    path('/products', views.products, name = 'products'),
    path('/store', views.store, name = 'store'),
    path('/cart', views.cart, name = 'cart'),
    path('/login', views.login, name = 'login'),
    path('/register', views.register, name = 'register'),
    path('/about', views.about, name = 'about'),
    path('/contact', views.contact, name = 'contact'),
    path('/view', views.view, name = 'view'),
    path('update_item/', views.updateItem, name = 'update_item'),
    path('', views.landingpage, name = 'home'),
    path('process_order', views.processOrder, name = 'process_order'),
]