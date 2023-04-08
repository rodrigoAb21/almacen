from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.FloatField()
    existencias = models.IntegerField(default=0)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + ' - precio:' + str(self.precio)
