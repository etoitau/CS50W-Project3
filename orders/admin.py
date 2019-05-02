from django.contrib import admin
from orders.models import Category, Size, MenuItem, Option, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(MenuItem)
admin.site.register(Option)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)