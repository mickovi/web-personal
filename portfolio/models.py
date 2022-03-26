from django.db import models

# Create your models here.
# Esta clase representa una tabla dentro de la BD
# Nombre de los modelos en singular, el admin lo pluraliza
# upload_to='projects': Crea una carpeta 'projects' dentro de 'media' donde guarda todas las imagenes

class Project(models.Model):
    title = models.CharField(verbose_name='Título', max_length=50)
    description = models.TextField(verbose_name='Descripción')
    link = models.URLField(verbose_name='Dirección Web', null=True, blank=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='projects', height_field=None, width_field=None, max_length=None)
    created = models.DateTimeField(verbose_name='Fecha de creación', auto_now=False, auto_now_add=True) # auto_now_add=True : Se agrega la fecha cuando se crea por primera vez
    updated = models.DateTimeField(verbose_name='Fecha de modificación', auto_now=True, auto_now_add=False) # auto_now_add=True : Se ejecuta cada vez que se modifica una instancia

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    # Mostrar el nombre del proyecto usando title
    def __str__(self):
        return self.title
