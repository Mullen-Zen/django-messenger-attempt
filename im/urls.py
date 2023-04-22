from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail")
]