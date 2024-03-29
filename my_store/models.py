from django.db import models

class Products(models.Model):
    categories = (
        ('Fruits', 'Fruits'),
        ('Meat', 'Meat'),
        ('Seafood', 'Seafood'),
        ('Vegetable', 'Vegetable'),

    )

    title = models.CharField(max_length=250)
    available = models.BooleanField()
    item_count = models.IntegerField()
    price = models.IntegerField(default=0)
    price_per = models.CharField(max_length=50, default='kg')
    product_category = models.CharField(max_length=100, default='Seafood', choices=categories)
    last_Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
