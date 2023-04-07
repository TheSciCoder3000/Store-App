from django.forms import ModelForm, modelformset_factory
from django import forms
from .models import Orders, OrderItem, Request, RequestItem, Products


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['add_message',]
        widgets = {
            'add_message': forms.Textarea(attrs={'placeholder': 'Put any additional request or info here.',
                                                  'class': 'message-form'})
        }

class OrderItemForms(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['item', 'quantity']
        widgets = {
            'item': forms.TextInput(attrs={'class': 'hidden'}),
            'quantity': forms.NumberInput(attrs={'class': 'hidden number-form'})
        }

OrderItemFormset = modelformset_factory(OrderItem,
                                        form=OrderItemForms,
                                        fields=['item', 'quantity'],
                                        extra=Products.objects.all().count())

class RequestForm(ModelForm):
    class Meta:
        model = Request
        exclude = ['Person', 'time_ordered',]
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'add your Block Lot and Phase HERE'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Mobile Number'}),
            'add_message': forms.TextInput(attrs={'placeholder': 'Put any additional request or info here.',
                                                  'class': 'message-form'})
        }

class RequestItemForms(ModelForm):
    class Meta:
        model = RequestItem
        fields = ['item', 'quantity']
