from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="shortify-index"),
    path("url/<str:shortenUrl>/", views.url, name="shortenUrl"),
]
