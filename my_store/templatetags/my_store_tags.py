from django import template

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
