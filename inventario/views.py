from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Marca, Instrumento
from .forms import CategoriaForm, MarcaForm, InstrumentoForm


from .models import Categoria, Marca, Instrumento


def inicio(request):
    contexto = {
        "total_categorias": Categoria.objects.count(),
        "total_marcas": Marca.objects.count(),
        "total_instrumentos": Instrumento.objects.count(),
        "ultimos_instrumentos": Instrumento.objects.select_related(
            "categoria", "marca"
        ).order_by("-id")[:5],
    }
    return render(request, "inventario/inicio.html", contexto)

#CATEGORÍAS
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        "inventario/lista.html",
        {"titulo": "Categorías", "items": categorias, "tipo": "categoria"},
    )


def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_categorias")
    return render(
        request,
        "inventario/formulario.html",
        {"form": form, "titulo": "Nueva Categoría"},
    )


def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect("lista_categorias")
    return render(
        request,
        "inventario/formulario.html",
        {"form": form, "titulo": "Editar Categoría"},
    )


def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect("lista_categorias")
    return render(
        request,
        "inventario/confirmar_eliminar.html",
        {"objeto": categoria, "cancelar_url": "lista_categorias"},
    )


#MARCAS
def lista_marcas(request):
    marcas = Marca.objects.all()
    return render(
        request,
        "inventario/lista.html",
        {"titulo": "Marcas", "items": marcas, "tipo": "marca"},
    )


def crear_marca(request):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_marcas")
    return render(
        request,
        "inventario/formulario.html",
        {"form": form, "titulo": "Nueva Marca"},
    )


def editar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    form = MarcaForm(request.POST or None, instance=marca)
    if form.is_valid():
        form.save()
        return redirect("lista_marcas")
    return render(
        request,
        "inventario/formulario.html",
        {"form": form, "titulo": "Editar Marca"},
    )


def eliminar_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == "POST":
        marca.delete()
        return redirect("lista_marcas")
    return render(
        request,
        "inventario/confirmar_eliminar.html",
        {"objeto": marca, "cancelar_url": "lista_marcas"},
    )


#INSTRUMENTOS
def lista_instrumentos(request):
    instrumentos = Instrumento.objects.select_related("categoria", "marca").all()
    return render(
        request,
        "inventario/lista.html",
        {"titulo": "Instrumentos", "items": instrumentos, "tipo": "instrumento"},
    )


def crear_instrumento(request):
    form = InstrumentoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_instrumentos")
    return render(
        request,
        "inventario/formulario.html",
        {"form": form, "titulo": "Nuevo Instrumento"},
    )


def editar_instrumento(request, pk):
    instrumento = get_object_or_404(Instrumento, pk=pk)
    form = InstrumentoForm(request.POST or None, instance=instrumento)
    if form.is_valid():
        form.save()
        return redirect("lista_instrumentos")
    return render(
        request,
        "inventario/formulario.html",
        {"form": form, "titulo": "Editar Instrumento"},
    )


def eliminar_instrumento(request, pk):
    instrumento = get_object_or_404(Instrumento, pk=pk)
    if request.method == "POST":
        instrumento.delete()
        return redirect("lista_instrumentos")
    return render(
        request,
        "inventario/confirmar_eliminar.html",
        {"objeto": instrumento, "cancelar_url": "lista_instrumentos"},
    )