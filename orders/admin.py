from django.contrib import admin
from orders.models import Category, Size, MenuItem, Option, Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(MenuItem)
admin.site.register(Option)
admin.site.register(Order)
admin.site.register(OrderItem)