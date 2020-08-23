from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserProfileForm
from my_store.models import Orders, Request, Products, OrderItem
from my_store.forms import OrderItemForms, OrderForm
from django.http import JsonResponse
from django.forms.models import modelformset_factory

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created! You can now Log In')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'users/register.html', {'form': form, 'profile_form': profile_form})

@login_required
def profile(request):
    context = {
        'orders': Orders.objects,
        'requests': Request.objects
    }
    return render(request, 'users/profile.html', context)

class OrderDetails(DetailView):
    model = Orders
    template_name = 'users/user_order_details.html'
    context_object_name = 'orders'

    def get_object(self, **kwargs):
        return Orders.objects.get(pk=self.kwargs['pk'])

    def get_order_pk(self, **kwargs):
        return self.kwargs['pk']

    def get_context_data(self, **kwargs):
        context = super(OrderDetails, self).get_context_data(**kwargs)
        context['items'] = Products.objects.all()

        my_order = OrderForm(instance=self.get_object())
        context['OrderForm'] = my_order

        order_Items = self.get_object().orderitem_set.all()
        context['order_items'] = order_Items

        OrderDetailFormset = modelformset_factory(OrderItem,
                                                  OrderItemForms,
                                                  fields=['item', 'quantity'],
                                                  extra=0)
        this_formset = OrderDetailFormset(queryset=OrderItem.objects.filter(order=self.get_object()))
        context['formset'] = this_formset

        return context

    def post(self, request, *args, **kwargs):
        OrderDetailFormset = modelformset_factory(OrderItem,
                                                  OrderItemForms,
                                                  fields=['item', 'quantity'],
                                                  extra=0)
        formset = OrderDetailFormset(request.POST or None)
        my_order = OrderForm(request.POST)

        if my_order.is_valid():
            user_order = self.get_object()
            message = my_order.cleaned_data['add_message']
            user_order.add_message = message
            user_order.save()
            print(message)

        for form in formset:
            instance = form.save(commit=False)
            instance.order = self.get_object()
            if instance.quantity == 0:
                instance.delete()
            else:
                instance.save()
        if formset.is_valid():
            formset.save()
        return redirect('user-order-detail', pk=self.get_order_pk())

class RequestDetails(DetailView):
    model = Request
    template_name = 'users/user_request_details.html'
    context_object_name = 'requests'

    def get_context_data(self, **kwargs):
        context = super(RequestDetails, self).get_context_data(**kwargs)
        context['items'] = Products.objects.all()
        return context

def order_request_delivered(request):
    if request.is_ajax():
        OR_ref_code = request.GET['data']
        if Orders.objects.filter(ref_code=OR_ref_code):
            order = Orders.objects.get(ref_code=OR_ref_code)
            order.completed = True
            order.save()
            print('\n\nDelivered\n\n')
        else:
            print('\n\nRequests\n\n')
        return JsonResponse({
            'delivered_msg': 'success'
        })
