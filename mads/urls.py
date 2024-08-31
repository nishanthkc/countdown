from django.urls import path

from mads.views import TestView

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", TestView.as_view()),
]