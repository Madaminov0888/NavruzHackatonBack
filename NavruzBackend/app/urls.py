from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [
    path("user/<str:uid>", views.AppUserSingleAPIView.as_view(), name = "user by id"),
    path("user/", views.AppUserSingleAPIView.as_view(), name="post user"),
    path("trashbins/", views.TrashBinsAPIView.as_view(), name = "Get all trash bins"),
]