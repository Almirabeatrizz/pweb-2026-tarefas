from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('another/', views.index, name="outra"),
    path('terceira/', views.index, name="terceira"),
]