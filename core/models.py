from django.db import models

# Create your models here.
class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_ciudad

class TipoDeInmueble(models.Model):
    tipo_de_inmueble = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo_de_inmueble

class Inmueble(models.Model):
    STATUS_CHOICES = [
        ('venta', 'venta'),
        ('renta', 'renta'),
    ]
    STATUS_VENTA_CHOICHES = [
        ('pendiente', 'pendiente'),
        ('publicado', 'publicado'),
        ('finalizado', 'finalizado'),
    ]
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    tipo_de_inmueble = models.ForeignKey(TipoDeInmueble, on_delete=models.CASCADE, null=True, blank=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    precio = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='renta')
    status_de_venta = models.CharField(max_length=20, choices=STATUS_VENTA_CHOICHES, default='publicado', null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)
    metros_cuadrados = models.IntegerField()
    banos = models.IntegerField(default=0, null=True)
    cuartos = models.IntegerField(default=0, null=True)
    cochera = models.IntegerField(default=0, null=True)
    dias_publicado = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.status_de_venta} "
  
    # exepcion que ocurrira al no encontrar la imagen
    @property
    def imagen_url(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url

class Dispositivo(models.Model):
    dispositivo_id = models.CharField(max_length=300)

class Favorito(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, null=True, blank=True)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=True, blank=True)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField()

class ImagenInmueble(models.Model):
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    imagen_inmueble = models.ImageField(null=True, blank=True)

class Contanto(models.Model):
    nombre = models.CharField(max_length=150)
    correo = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre