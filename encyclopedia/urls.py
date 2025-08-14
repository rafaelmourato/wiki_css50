from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("newPage", views.newPage, name="newpage"),
    path("page", views.newPage, name="page"),
    path("editPage/<str:title>/", views.editPage, name="editpage"),
    path("random", views.randomPage, name="randomPage"),
    path("notFound", views.page, name="notFound"),
    path("<str:page>", views.page, name="page")
]
