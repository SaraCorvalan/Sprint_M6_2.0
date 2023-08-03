from django.shortcuts import render,redirect
from aplicacion.models import registroClientes, Proveedores
from django.contrib.auth import authenticate, login
from .forms import registroForm, proveedoresForm, LoginForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def ir_a_vista_admin(request):
    # Redirige al usuario a la vista de administración
    return redirect('/admin/')
# Decoradores para verificar si el usuario pertenece a cada grupo respectivamente
def user_is_admin(user):
    return user.groups.filter(name='grupo6').exists()

def user_is_contabilidad(user):
    return user.groups.filter(name='contabilidad').exists()

def user_is_comercial(user):
    return user.groups.filter(name='comercial').exists()

def login_redirect(request):
    if request.user.groups.filter(name='grupo6').exists():
        return redirect('/admin/')
    elif request.user.groups.filter(name='contabilidad').exists():
        return redirect('landing.html')
    elif request.user.groups.filter(name='comercial').exists():
        return redirect('landing.html')
    else:
        # Si el usuario no pertenece a ningún grupo, redirige a una página predeterminada
        return redirect('pagina_predeterminada')
def vista_comercial(request):
    return render(request, 'vista_comercial.html')

#  CLIENTES
def primeraFuncion(request):
    return render(request, 'landing.html')

@login_required
def formularioContacto(request):
    data = {
        'form': registroForm()
    }
    if request.method == 'POST':
        formulario = registroForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "USUARIO REGISTRADO !!!"
        else:
            data["form"] = formulario
    return render(request, 'registro_clientes.html', data)


@login_required
def informeClientes(request):
     #'usuarios' es una instancia de la clase "registroUsuarios" definida en models.py
    usuarios = registroClientes.objects.all()
    return render(request, 'salida_clientes.html', {'usuarios': usuarios})
##############################################################################################
# EMPRESAS PROVEEDORAS

@login_required
def registroProveedores(request):
    data = {
        'form_prov': proveedoresForm()
    }
    if request.method == 'POST':
        formulario_prov = proveedoresForm(data=request.POST)
        if formulario_prov.is_valid():
            formulario_prov.save()
            data["mensaje"] = "PROVEEDOR REGISTRADO !!!"
        else:
            data["form_prov"] = formulario_prov
    return render(request, 'registro_empresa.html', data)

@login_required
def informeProveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'salida_empresas.html', {'proveedores': proveedores})
##############################################################################################
# USERS
def user_login(request):
    
    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
           usuario = formulario.cleaned_data['usuario']
           password = formulario.cleaned_data['password']
           user = authenticate(request, username=usuario, password=password)
           if user is not None:
               if user.is_active:
                   login(request, user)
                   #messages.success(request, f"Autentificación exitosa, estimado(a) {usuario}")
                   return render(request, 'vista_comercial.html', {'users': usuario})
                   #return HttpResponse(f"Autentificación exitosa, estimado(a) {usuario}")
               else:
                   messages.error(request, "Cuenta no habilitada")
                   #return HttpResponse("Cuenta NO habilitada")
           else:
               #return HttpResponse("Login No válido")
                messages.error(request, "Login no válido")
    else:
        formulario = LoginForm()

    return render(request, 'registration/login.html', {'formulario': formulario})

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }   
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
           formulario.save()
           usuario = formulario.cleaned_data['username']
           password = formulario.cleaned_data['password1']
           user = authenticate(request, username=usuario, password=password)       
           login(request, user)
           return render(request, 'landing.html', {'users': usuario})
           messages.success(request, f"Te has registrado correctamente, estimado(a) {usuario}")           
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)