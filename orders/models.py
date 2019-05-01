import json

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Category(models.Model):
    """categories of menu items"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Size(models.Model):
    """available sizes"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class MenuItem(models.Model):
    """menu items"""
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    option_num = models.SmallIntegerField(default=0)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.size} {self.name} {self.category} for ${self.price}'

    def jsonObj(self):
        """return a json version of object"""
        obj = {
            "category": self.category.name,
            "name": self.name,
            "price": float(self.price),
            "option_num": self.option_num,
            "size": self.size.name,
        }
        return json.dumps(obj)


class Option(models.Model):
    """available options for menuitems in a category"""
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.category}: {self.name}'


class Order(models.Model):
    """an order placed by a client"""
    client = models.ForeignKey(User, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)
    bill = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        # note error appears to be pylint bug, works fine
        return f'{self.timestamp} - {self.client.first_name} {self.client.last_name} - ${self.bill} - Fulfilled: {self.fulfilled}'

class OrderItem(models.Model):
    """an item in an order"""
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu_item = models.ManyToManyField(MenuItem, related_name="order_items")
    options = models.CharField(max_length=512, default=None)
    
    def set_options(self, opts):
        """given a list of options, includes as a json object"""
        self.options = json.dumps(opts)
    
    def get_opts(self):
        """retrieves options from string"""
        return json.loads(self.options)
    
    def __str__(self):
        return f'{self.menu_item} with: {self.options}'






