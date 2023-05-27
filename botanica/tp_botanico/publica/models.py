from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True,max_length=8)
    actividad = [
        ("V", "Cliente VIP"),
        ("R", "Regular"),
        ("N", "No Compra"),
    ]
    numero_socio = models.IntegerField()
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    dni = models.CharField(max_length=10,unique=True,verbose_name='Dni')
    email = models.EmailField(max_length=256,null=True,verbose_name='Email')
    te = models.CharField(max_length=20,verbose_name='Telefono')
    activo = models.CharField(max_length=1, choices=actividad)
    fecha_reg = models.DateField(null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    fecha_ultima_compra = models.DateField(null=True, blank=True)
    fecha_ultimo_login =  models.DateField(null=True, blank=True)
    baja = models.BooleanField(default=0)

    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()    


class Planta(models.Model):

    lugar = [
        ("I","Interior"),
        ("E","Exterior"),
        ("C","Cualquiera"),
    ]
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    descripcion = models.TextField(max_length=1000, help_text="Describa la planta")
    ambiente = models.CharField(max_length=1, choices=lugar)
    imagen= models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True)
    


class Categoria(models.Model):
    tipo = models.CharField(max_length=50,verbose_name='Tipo')    
    descripcion = models.TextField(max_length=1000, help_text="Describa las Propiedades de la categoría")

class Producto(models.Model):
    cod_producto = models.IntegerField()
    categorias = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    planta =models.ForeignKey(Planta,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    cod_categ = models.CharField(max_length=10,unique=True)
    descripcion = models.TextField(max_length=1000, help_text="Describa las Propiedades del Producto")
    precio = models.CharField(max_length=200)
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='foto_prod/',null=True,verbose_name='Foto Producto')


class Kits(models.Model):
    nombre = models.CharField(max_length=100,verbose_name="Nombre")
    descripcion = models.TextField(max_length=1000, help_text="Describa para que sirve el kit")
   # kproducto_principal = models.ForeignKey(Producto,on_delete=models.CASCADE)
    accesorios  = models.ManyToManyField(Producto) 