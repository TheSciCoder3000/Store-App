from django.forms import ModelForm
from django import forms
from .models import Orders, Products

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        exclude = ['Person', 'time_ordered',]
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'add your Block Lot and Phase HERE'}),
        }

        for item in Products.objects.all():
            widgets[item.title] = forms.CheckboxInput(attrs={'onclick': "hide_me('{}')".format(item.title),
                                                       'id': '{}-checkbox'.format(item.title)})

            widgets[item.title+'_counter'] = forms.NumberInput(attrs={'class': 'number-form',
                                                                      'step': '.01'})
