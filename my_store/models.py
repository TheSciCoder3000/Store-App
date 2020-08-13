from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Products(models.Model):
    categories = (
        ('Fruits', 'Fruits'),
        ('Meat', 'Meat'),
        ('Seafood', 'Seafood'),
        ('Vegetable', 'Vegetable'),

    )

    title = models.CharField(max_length=250)
    available = models.BooleanField()
    item_count = models.FloatField()
    price = models.FloatField(default=0)
    price_per = models.CharField(max_length=50, default='kg')
    product_category = models.CharField(max_length=100, default='Seafood', choices=categories)
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
    Person = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.TextField(null=True)
    number = models.IntegerField(null=True)
    time_ordered = models.DateTimeField(default=timezone.now)
    item_list = [it.title for it in Products.objects.all()]
    for item in item_list:
        vars()[item] = models.BooleanField(default=False)
        vars()[item+'_counter'] = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.Person)

    class Meta:
        verbose_name_plural = "Orders"

class Request(models.Model):
    Person = models.ForeignKey(User, on_delete=models.PROTECT)
    address = models.TextField(null=True)
    number = models.IntegerField(null=True)
    time_ordered = models.DateTimeField(default=timezone.now)
    item_list = [it.title for it in Products.objects.all()]
    for item in item_list:
        vars()[item] = models.BooleanField(default=False)
        vars()[item+'_counter'] = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.Person)

    class Meta:
        verbose_name_plural = "Requests"
