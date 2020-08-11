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
