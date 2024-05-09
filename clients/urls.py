from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('clients/', views.show_clients, name="show_clients"),
    path('clients/details/<int:id>', views.details, name="details"),
]
