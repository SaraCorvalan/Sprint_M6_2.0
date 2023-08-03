from django.urls import path
from aplicacion.views import *
from django.contrib.auth import views


urlpatterns = [
    path('', primeraFuncion, name = 'index'),
    path('registro_clientes/login/', primeraFuncion, name = 'index'),
    path('salida/login/', primeraFuncion, name = 'index'),
    path('registro_empresa/login/', primeraFuncion, name = 'index'),
    path('salida_empresas/login/', primeraFuncion, name = 'index'),
    path('registro_clientes/', formularioContacto, name = 'registro_clientes'),
    path('salida_clientes/', informeClientes, name = 'salida_clientes'),
    path('registro_empresa/', registroProveedores, name = 'registro_empresa'),
    path('salida_empresas/', informeProveedores, name = 'salida_empresas'),
    path('login/', user_login, name = 'login'),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
    path('comercial/', vista_comercial, name='vista_comercial'),
    
]