from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from django.forms import formset_factory
from .models import OrderItem, Products, Orders, Request, HomeImage
from django.http import JsonResponse
import json
from pytz import timezone
import datetime


day_indx = datetime.datetime.now(timezone('Hongkong')).weekday()
sell_day = 5

def home(request):
    return render(request, 'my_store/home.html', {'home_images': HomeImage.objects.all()})

def store(request):

    if request.is_ajax() and request.method == 'POST':
        return JsonResponse({
            'msg': 'success'
        })

    if request.method == 'POST':
        orderlist_form = OrderForm(request.POST, prefix='orders')
        formset = OrderItemFormset(request.POST)
        user = request.user
        order, created = Orders.objects.get_or_create(Person=user, completed=False)
        if created:
            order.address = user.userprofile.Location
            order.number = user.userprofile.Contact_Number
            order.save()

        if orderlist_form.is_valid():
            add_mess = orderlist_form.cleaned_data['add_message']
            if add_mess:
                print('adding message')
                order.add_message += '\n\n'+add_mess
                order.save()

        if formset.is_valid():                                                  # If valid, create or update Order Items
            for form in formset:
                if bool(form.cleaned_data):
                    item = form.cleaned_data['item']
                    if OrderItem.objects.filter(order=order, item=item):
                        quantity = form.cleaned_data['quantity']
                        my_item = OrderItem.objects.get(order=order, item=item)
                        my_item.quantity = float(my_item.quantity ) + float(quantity)
                        my_item.save()
                    else:
                        form.save()
                    instance = form.save(commit=False)
                    instance.order = order
                    instance.save()

            return redirect('store-store')
    else:
        formset = OrderItemFormset(queryset=OrderItem.objects.none())
        orderlist_form = OrderForm(prefix='orders')

    context = {
        'title': 'Store',
        'prod': Products.objects.all(),
        'products': Products.objects.all(),
        'formset': formset,
        'orderForm': orderlist_form,
        'mylist': zip(formset, Products.objects.all()),
        'btn_title': 'Order',
    }
    return render(request, 'my_store/store.html', context)

def deactivate_btn(request):
    if request.is_ajax():
        return JsonResponse({
            'msg': 'success'
        })

def update_item(request):
    print('Creating')
    data = json.loads(request.body)
    ItemId = data['productid']
    action = data['action']

    owner = request.user
    prod = Products.objects.get(id=ItemId)
    order, created = Orders.objects.get_or_create(Person=owner, completed=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, item=prod)

    if action == 'delete':
        orderItem.delete()
    return JsonResponse('Success', safe=False)

@staff_member_required
def orders_to_admin(request):
    context = {
        'items': Products.objects.all(),
        'data_name': 'Orders',
        'table_data': Orders.objects.all()
    }
    return render(request, 'my_store/orders_admin_only.html', context)

@staff_member_required
def requests_to_admin(request):
    context = {
        'items': Products.objects.all(),
        'data_name': 'Orders',
        'table_data': Request.objects.all()
    }
    return render(request, 'my_store/requests_admin_only.html', context)

class OrderDetails(DetailView):
    model = Orders
    template_name = 'my_store/order_details.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super(OrderDetails, self).get_context_data(**kwargs)
        context['items'] = Products.objects.all()
        return context

class RequestDetails(DetailView):
    model = Request
    template_name = 'my_store/request_details.html'
    context_object_name = 'requests'

    def get_context_data(self, **kwargs):
        context = super(OrderDetails, self).get_context_data(**kwargs)
        context['items'] = Products.objects.all()
        return context

class ProductDetails(DetailView):
    model = Products
    template_name = "my_store/prod_details.html"
    context_object_name = 'product'
