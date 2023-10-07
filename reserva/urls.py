from django.urls import path, include
from . import views

urlpatterns = [
    path("painel/", views.eventos, name="reserva"),
    path("analise/", views.analise)
]


