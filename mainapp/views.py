from django.views.generic import TemplateView
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


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
