from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def home(request):
    return render(request, 'my_store/home.html')

def store(request):
    context = {
        'title': 'Store',
        'prod': Products.objects.all(),
        'categories': [category[1] for category in Products._meta.get_field('product_category').choices],
        'prod_model': Products,
    }

    return render(request, 'my_store/store.html', context)
