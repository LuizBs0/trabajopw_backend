from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('restaurantes', views.restaurantes),
    path('platos', views.platos),
    path('platos/categorias', views.categoria_pla),
    path('restaurantes/categorias', views.categoria_res),
    path('usuarios', views.listaUsuarios)
]