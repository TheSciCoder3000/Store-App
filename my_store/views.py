from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OrderForm
from .models import Products, Orders


def home(request):
    return render(request, 'my_store/home.html')

def store(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        instance = form.save(commit=False)
        instance.Person = request.user
        if form.is_valid():
            form.save()
            return redirect('store-store')
    else:
        form = OrderForm()

    context = {
        'title': 'Store',
        'prod': Products.objects.all(),
        'form': form,
        'prod_model': Products,
    }

    return render(request, 'my_store/store.html', context)

@staff_member_required
def to_admin(request):
    context = {
        'items': Products.objects.all(),
        'Orders': Orders.objects.all()
    }
    return render(request, 'my_store/admin_only.html', context)
