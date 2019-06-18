from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="shortify-index"),
    path("url/<str:shortedUrl>/", views.url, name="shortedUrl"),
    path("api/get", views.get, name="url-get"),
    path("api/post", views.post, name="url-post"),
    path("api/delete", views.delete, name="url-delete"),
]
