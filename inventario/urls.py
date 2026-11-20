from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("categorias/", views.lista_categorias, name="lista_categorias"),
    path("categorias/nueva/", views.crear_categoria, name="crear_categoria"),
    path("categorias/editar/<int:pk>/", views.editar_categoria, name="editar_categoria"),
    path("categorias/eliminar/<int:pk>/", views.eliminar_categoria, name="eliminar_categoria"),
    path("marcas/", views.lista_marcas, name="lista_marcas"),
    path("marcas/nueva/", views.crear_marca, name="crear_marca"),
    path("marcas/editar/<int:pk>/", views.editar_marca, name="editar_marca"),
    path("marcas/eliminar/<int:pk>/", views.eliminar_marca, name="eliminar_marca"),
    path("instrumentos/", views.lista_instrumentos, name="lista_instrumentos"),
    path("instrumentos/nuevo/", views.crear_instrumento, name="crear_instrumento"),
    path("instrumentos/editar/<int:pk>/", views.editar_instrumento, name="editar_instrumento"),
    path("instrumentos/eliminar/<int:pk>/", views.eliminar_instrumento, name="eliminar_instrumento"),
]