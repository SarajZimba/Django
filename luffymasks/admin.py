from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(product)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)