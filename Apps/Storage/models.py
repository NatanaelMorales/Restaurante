from django.db import models

# Create your models here.

class Bebidas(models.Model):
    pk_bebidas = models.AutoField(primary_key=True, null=False, blank=False)
    codigo = models.CharField(max_length=9, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen1 = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    precio = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)

    class Meta:
        verbose_name='bebida'
        verbose_name_plural='bebidas'
        ordering=['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)

class Postres(models.Model):
    pk_postres = models.AutoField(primary_key=True, null=False, blank=False)
    codigo_post = models.CharField(max_length=9, null=False, blank=False)
    nombre_post = models.CharField(max_length=40, null=False, blank=False)
    descripcion_post = models.TextField(null=False, blank=False)
    imagen1_post = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    precio_post = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)

    class Meta:
        verbose_name='postre'
        verbose_name_plural='postres'
        ordering=['nombre_post']

    def __str__(self):
        return "{0}".format(self.nombre_post)

class Extras(models.Model):
    pk_extras = models.AutoField(primary_key=True, null=False, blank=False)
    codigo_ext = models.CharField(max_length=9, null=False, blank=False)
    nombre_ext = models.CharField(max_length=40, null=False, blank=False)
    descripcion_ext = models.TextField(null=False, blank=False)
    imagen1_ext = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    precio_ext = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)

    class Meta:
        verbose_name='extra'
        verbose_name_plural='extras'
        ordering=['nombre_ext']

    def __str__(self):
        return "{0}".format(self.nombre_ext)