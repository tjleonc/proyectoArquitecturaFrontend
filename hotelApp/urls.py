from django.urls import path
from hotelApp import views

urlpatterns = [
    path('', views.index, name="Inicio"),
]