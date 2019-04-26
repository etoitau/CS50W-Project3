from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


import json

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Size(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.name}'


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    option_num = models.SmallIntegerField(default=0)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.size} {self.name} {self.category} for ${self.price}'


class Option(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.category}: {self.name}'


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)
    bill = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        # note error appears to be pylint bug, works fine
        return f'{self.timestamp} - {self.client.first_name} {self.client.last_name} - ${self.bill} - Fulfilled: {self.fulfilled}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_item = models.ManyToManyField(Order, related_name="order_items")
    options = models.CharField(max_length=512, default=None)
    
    def set_options(self, opts):
        self.options = json.dumps(opts)
    
    def get_opts(self):
        return json.loads(self.options)
    
    def __str__(self):
        return f'{self.menu_item} with: {self.options}'






