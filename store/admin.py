from django.contrib import admin

# Register your models here.
from store.models import *

admin.site.register(Product)
admin.site.register(ProductImg)
admin.site.register(Category)
# admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(CheckOut)
