from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:page>", views.page, name="page"),
    path("/newPage", views.newPage, name="newpage"),
    path("/editPage", views.editPage, name="editpage"),
    path("/random", views.randomPage, name="randomPage"),
    path("/notFound", views.page, name="notFound")
]
