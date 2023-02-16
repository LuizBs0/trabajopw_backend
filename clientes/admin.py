from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Categoria_Pla)
admin.site.register(models.Categoria_Res)
admin.site.register(models.Restaurante)
admin.site.register(models.Plato)
admin.site.register(models.Usuario)