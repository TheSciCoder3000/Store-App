from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class PrductCategory(models.Model):
    CategoryTitle = models.CharField(max_length=20)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.CategoryTitle

    class Meta:
        verbose_name_plural = 'Product Categories'

class Products(models.Model):
    title = models.CharField(max_length=250)
    available = models.BooleanField()
    item_count = models.FloatField(default=0)
    price = models.FloatField(default=0)
    price_per = models.CharField(max_length=50, default='kg')
    product_category = models.ForeignKey(PrductCategory, default='None', on_delete=models.SET_DEFAULT)
    last_Updated = models.DateTimeField(auto_now=True)
    item_thresh = models.FloatField(blank=True, null=True)
    discount = models.FloatField(default=0.1)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['product_category', 'title']
        verbose_name_plural = "Products"

class Orders(models.Model):
    def get_uuid():
        return uuid.uuid4().hex[:25].upper()
    Person = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=25, default=get_uuid, null=True, unique=True)
    completed = models.BooleanField(default=False)
    address = models.TextField(null=True)
    number = models.IntegerField(null=True)
    add_message = models.TextField(null=True, blank=True)
    time_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {}".format(str(self.Person), self.ref_code)

    class Meta:
        verbose_name_plural = "Orders"

class Request(models.Model):
    def get_uuid():
        return uuid.uuid4().hex[:25].upper()
    Person = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=25, default=get_uuid, null=True, unique=True)
    completed = models.BooleanField(default=False)
    address = models.TextField(null=True)
    number = models.IntegerField(null=True)
    add_message = models.TextField(null=True, blank=True)
    time_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {}".format(str(self.Person), self.ref_code)

    class Meta:
        verbose_name_plural = "Requests"

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10000, decimal_places=2, null=True)

    def __str__(self):
        try:
            owner, ref_code = str(self.order).split(' - ')
        except:
            ref_code = 'None'
        return "{} - {}".format(self.item, ref_code)

    def get_total(self):
        item_price = self.item.price
        return float(item_price)*float(self.quantity)

    def get_owner(self):
        owner, ref_code = str(self.order).split(' - ')
        return owner

class RequestItem(models.Model):
    request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10000, decimal_places=2, null=True)

    def __str__(self):
        try:
            owner, ref_code = str(self.request).split(' - ')
        except:
            ref_code = 'None'
        return "{} - {}".format(self.item, ref_code)

    def get_total(self):
        item_price = self.item.price
        return float(item_price)*float(self.quantity)

    def get_owner(self):
        owner, ref_code = str(self.order).split(' - ')
        return owner

class HomeImage(models.Model):
    image_name = models.CharField(max_length=25)
    my_image = models.ImageField()

    def __str__(self):
        return self.image_name
