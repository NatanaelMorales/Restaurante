from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResourceBebida(resources.ModelResource):
    class Meta:
        model = Bebidas

class AdminBebida(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_bebidas', 'codigo', 'nombre', 'descripcion', 'precio']
    resource_class = ResourceBebida

admin.site.register(Bebidas, AdminBebida)

class ResourcePostre(resources.ModelResource):
    class Meta:
        model = Postres

class AdminPostre(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['nombre_post']
    list_display=['pk_postres', 'codigo_post', 'nombre_post', 'descripcion_post', 'precio_post']
    resource_class = ResourcePostre

admin.site.register(Postres, AdminPostre)

class ResourceExtra(resources.ModelResource):
    class Meta:
        model = Extras

class AdminExtra(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields=['nombre_ext']
    list_display=['pk_extras', 'codigo_ext', 'nombre_ext', 'descripcion_ext', 'precio_ext']
    resource_class = ResourceExtra

admin.site.register(Extras, AdminExtra)