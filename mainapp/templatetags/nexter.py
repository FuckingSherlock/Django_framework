import json

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

with open("Django_framework/templates/news.json", "r") as f:
    news = json.loads(f.read())


def news_generate():
    for item in news:
        title = item
        descript = news[item][0]
        link = news[item][1]
        time = news[item][2]
        news_list = [title, descript, link, time]
        yield news_list


@register.filter
def nexter(type):
    counter = news["counter"]
    if type == "link":
        news["counter"] += 1
        if counter > 10:
            news["counter"] = 0
    return mark_safe(f"{news[type][counter]}")
