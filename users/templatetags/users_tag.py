from django import template

register = template.Library()

@register.filter
def data_by_user(OR, user):
    return OR.filter(Person=user)
