from datetime import datetime

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def datetime_new(value):
    time = value.split(",")[0]
    date = "".join(str(datetime.now().date()).replace("-", " / ").split(" ")[::-1])
    dt = time + " " + date
    return mark_safe(f"{dt}")
