from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    autor = models.CharField(max_length=100, verbose_name='autor', null=True)
    
    def __str__(self):
        fila = f"Titulo: {self.titulo} - Descripcion: {self.descripcion} - Autor: {self.autor}"
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        
    