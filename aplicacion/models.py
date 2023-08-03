from django.db import models

# Create your models here.
class registroClientes(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=8)
    creacion = models.DateField(auto_now_add=True)                         
    def __str__(self):
        return "Usuario RUT %s y nombre %s %s" %(self.rut, self.nombre, self.apellido)


class Proveedores(models.Model):
    rut_empresa = models.CharField(max_length=10, unique=True)
    nombre_empresa = models.CharField(max_length=40)
    direccion_empresa = models.CharField(max_length=60)
    ciudad_empresa = models.CharField(max_length=30)
    email_empresa = models.EmailField(max_length=40)
    fono_empresa = models.CharField(max_length=12)
    rubro_empresa = models.CharField(max_length=50)                           
    def __str__(self):
        return "Empresa proveedora RUT: %s, nombre: %s, email: %s, teléfono: %s, rubro: %s" %(self.rut_empresa, self.nombre_empresa, self.email_empresa, self.fono_empresa, self.rubro_empresa)