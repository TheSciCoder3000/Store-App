from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OrderForm, RequestForm
from .models import Products, Orders, Request, HomeImage
from pytz import timezone
import datetime


day_indx = datetime.datetime.now(timezone('Hongkong')).weekday()
sell_day = 5

def home(request):
    return render(request, 'my_store/home.html', {'home_images': HomeImage.objects.all()})

def store(request):
    if request.method == 'POST':
        if day_indx == sell_day:
            form = OrderForm(request.POST)
        else:
            form = RequestForm(request.POST)
        instance = form.save(commit=False)
        instance.Person = request.user
        if form.is_valid():
            form.save()
            return redirect('store-store')
    else:
        if day_indx == sell_day:
            form = OrderForm()
            btn_title = 'Order'
        else:
            form = RequestForm()
            btn_title = 'Request'

    context = {
        'title': 'Store',
        'prod': Products.objects.all(),
        'form': form,
        'prod_model': Products,
        'btn': btn_title,
    }

    return render(request, 'my_store/store.html', context)

@staff_member_required
def to_admin(request):
    if day_indx == sell_day:
        tdata = Orders.objects.all()
        dname = 'Orders'
    else:
        tdata = Request.objects.all()
        dname = 'Requests'
    context = {
        'items': Products.objects.all(),
        'data_name': dname,
        'table_data': tdata
    }
    return render(request, 'my_store/admin_only.html', context)

class OrderDetails(DetailView):
    model = Orders
    template_name = 'my_store/order_details.html'
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super(OrderDetails, self).get_context_data(**kwargs)
        context['items'] = Products.objects.all()
        return context
