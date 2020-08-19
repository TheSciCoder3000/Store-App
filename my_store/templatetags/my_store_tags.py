from django import template
from ..models import *
from ..forms import OrderItemForms

register = template.Library()

@register.filter
def cat_filter(value, argv):
    return value.filter(product_category=argv)

@register.filter
def is_available(value):
    if value:
        return 'Available'
    else:
        return 'Not Available'

@register.simple_tag
def order_field(form, item_field):
    return form.__getitem__(item_field)

@register.simple_tag
def order_counter(form, item_field):
    return form.__getitem__(item_field+'_counter')

@register.filter
def is_order_avail(item, order):
    item_state = getattr(order, item.title)
    return item_state

@register.simple_tag
def get_order_counter(item, order):
    item_counter = getattr(order, item.title+'_counter')
    return item_counter

@register.simple_tag
def get_field(my_form, fieldname):
    return my_form.__getitem__(fieldname)

@register.filter
def data_by_user(OR):
    return OR.orderitem_set.all()

@register.filter
def get_OR_owner(OR):
    return OR.get_owner()

@register.filter
def get_items_totals(orderList):
    items = [x.quantity for x in orderList.orderitem_set.all()]
    total = sum(items)
    if total % 1 == 0:
        return int(total)
    else:
        return total
