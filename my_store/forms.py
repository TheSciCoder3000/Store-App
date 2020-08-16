from django.forms import ModelForm
from django import forms
from .models import Orders, Products, Request

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        exclude = ['Person', 'time_ordered',]
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'add your Block Lot and Phase HERE'}),
            'number': forms.NumberInput(attrs={'placeholder': 'Mobile Number'}),
            'add_message': forms.TextInput(attrs={'placeholder': 'Put any additional request or info here.',
                                                  'class': 'message-form'})
        }

        for item in Products.objects.all():
            widgets[item.title] = forms.CheckboxInput(attrs={'onclick': "hide_me('{}')".format(item.title),
                                                             'onload': "hide_me('{}')".format(item.title),
                                                             'id': '{}-checkbox'.format(item.title)})

            widgets[item.title+'_counter'] = forms.NumberInput(attrs={'class': 'number-form',
                                                                      'step': '.01',
                                                                      'id': 'form-{}-counter'.format(item.title),
                                                                      'onkeyup': "check_price('{}',{}, {})".format(item.title, item.item_thresh, item.discount),})


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

        for item in Products.objects.all():
            widgets[item.title] = forms.CheckboxInput(attrs={'onclick': "hide_me('{}')".format(item.title),
                                                             'onload': "hide_me('{}')".format(item.title),
                                                             'id': '{}-checkbox'.format(item.title)})

            widgets[item.title+'_counter'] = forms.NumberInput(attrs={'class': 'number-form',
                                                                      'step': '.01',
                                                                      'id': 'form-{}-counter'.format(item.title),
                                                                      'onkeyup': "check_price('{}',{}, {})".format(item.title, item.item_thresh, item.discount),})
