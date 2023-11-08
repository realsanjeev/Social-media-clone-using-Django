from django import template

register = template.Library()

@register.filter
def minus(value, args):
    return value - args