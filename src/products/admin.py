from django.contrib import admin

# Register your models here.
from .models import Caracteristica, Product, Categoria, SubCategoria, Presentacion, CategoriaCultura, EntradasCultura

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    readonly_fields = ('id',)

@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    readonly_fields = ('id',)

@admin.register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
    list_display = ('caracteristica',)
    readonly_fields = ('id',)    

@admin.register(Presentacion)
class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('presentacion',)
    readonly_fields = ('id',)


@admin.register(CategoriaCultura)
class CategoriaCulturaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('id',)

@admin.register(EntradasCultura)
class EntradasCulturaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    readonly_fields = ('id',)    