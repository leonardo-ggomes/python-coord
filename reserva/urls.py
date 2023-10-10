from django.urls import path
from . import views

urlpatterns = [
    path("painel/", views.eventos, name="reserva"),
    path("analise/", views.analise, name="analise")
]


