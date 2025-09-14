from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # columnas que quieres ver en la lista
    list_display = ('id', 'nombre', 'email', 'fono')

    # campos por los que se puede buscar
    search_fields = ('nombre', 'email')

    # filtros en la barra lateral
    list_filter = ('nombre',)

    # orden por defecto (primero los más recientes)
    ordering = ('-id',)
