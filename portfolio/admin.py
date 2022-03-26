from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # Muestra los campos de solo lectura

admin.site.register(Project, ProjectAdmin) # (App, configuración extendida)