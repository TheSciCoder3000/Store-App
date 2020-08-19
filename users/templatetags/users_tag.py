from django import template
from my_store.models import Products, Orders

register = template.Library()

@register.filter
def zip_list(list1, list2):
    return zip(list1, list2)

@register.filter
def data_by_user(OR):
    return OR.orderitem_set.all()

@register.filter
def request_by_user(request):
    return request.requestitem_set.all()

@register.filter
def get_product_data(item, data):
    return getattr(item.item, data)

@register.filter
def get_item_total(item):
    return item.get_total()

@register.filter
def user_data(orderList, user):
    return orderList.filter(Person=user)

@register.filter
def get_field(my_form, fieldname):
    return my_form.__getitem__(fieldname)
