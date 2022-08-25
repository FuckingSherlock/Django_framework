from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="index"),
    path("новости/", views.NewsPageView.as_view(), name="news"),
    path("курсы/", views.CoursesPageView.as_view(), name="courses_list"),
    path("контакты/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
]
