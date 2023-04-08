from django.contrib import admin
from app1.models import Categoria, Producto

# Register your models here.
admin.site.register(Categoria)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'existencias', 'categoria_id')
    list_display_links = ['nombre']
    search_fields = ['nombre']
    
admin.site.register(Producto, ProductoAdmin)
