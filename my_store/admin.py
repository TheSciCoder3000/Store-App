from django.contrib import admin
from .models import Products, Orders


def make_avail(modeladmin, request, queryset):
    for item in queryset:
        if item.available:
            item.available = False
        else:
            item.available = True
        item.save()
make_avail.short_description = "Select Available Products"

class The_Prod_Cat(admin.ModelAdmin):
    list_display = ('title', 'Product_Catgeory', 'Price', 'available')
    search_fields = ('title',)
    list_filter = ('product_category',)
    actions = (make_avail,)

    def Product_Catgeory(self, obj):
        return obj.product_category

    def Price(self, obj):
        return obj.price

admin.site.register(Products, The_Prod_Cat)

admin.site.register(Orders)
