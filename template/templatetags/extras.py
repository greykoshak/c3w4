from django import template

register = template.Library()

@register.filter(name='inc')
def inc(a, b):
    try:
        a = int(a)
        b = int(b)
    except (ValueError, TypeError):
        return 'Error'

    return a + b


@register.simple_tag
def division(a, b, to_int=False):
    a = int(a)
    b = int(b)

    if b != 0:
        return a//b if to_int is True else a/b

    return 'Error'