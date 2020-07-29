from django import template
from django.utils.safestring import mark_safe

register = template.Library()   # register的名字是固定的,不可改变


@register.filter
def my_filter(v1, v2):
    if v1.isdigit():
        return v1 * v2
    else:
        return v1[:2]


@register.simple_tag
def my_tag1(v1, v2, v3):
    # return v1 * v2 * v3
    temp_html = "<input type='text' id='%s' class='%s' _d='%s''/>" %(v1, v2, v3)
    return mark_safe(temp_html)

