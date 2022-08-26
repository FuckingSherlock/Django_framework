import json
from datetime import datetime

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open("Django_framework/templates/news.json", "r") as f:
            news = json.loads(f.read())

        context["news_new"] = news
        # Get all previous data
        # Create your own data
        context["news_title"] = "head"
        context["news_preview"] = "descr"
        context["range"] = range(5)
        context["datetime_obj"] = datetime.now()
        print(context)
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
