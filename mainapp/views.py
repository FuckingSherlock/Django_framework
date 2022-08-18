from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello world")


class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hello world")


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")
