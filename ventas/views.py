from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import AddClienteForm, EditarClienteForm, AddProductoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def ventas_view(request):
    num_ventas = 156
    context = {
        'num_ventas' : num_ventas
    }
    return render(request, 'ventas.html', context)

@login_required
def clientes_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForm()

    context = {
        'clientes':clientes,
        'form_personal': form_personal,
        'form_editar' : form_editar
    }
    return render(request, 'clientes.html', context)

@login_required
def add_cliente_view(request):
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al Guardar el Cliente")
                return redirect('Clientes')
    return redirect('Clientes')

@login_required
def edit_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForm(
            request.POST, request.FILES, instance=cliente)
        if form.is_valid:
            form.save()
    return redirect('Clientes')

@login_required
def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect('Clientes')

@login_required
def productos_view(request):
    productos = Producto.objects.all()
    form_add = AddProductoForm()
    context = {
        'productos': productos,
        'form_add' : form_add
    }
    return render(request, 'productos.html', context)

@login_required
def add_producto_view(request):
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al Guardar el Producto")
                return redirect('Clientes')
    return redirect('Productos')

@login_required
def delete_producto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_producto_eliminar'))
        producto.delete()
    return redirect('Productos')

@login_required
def salir (request):
    logout(request)
    return redirect('Clientes')

    
