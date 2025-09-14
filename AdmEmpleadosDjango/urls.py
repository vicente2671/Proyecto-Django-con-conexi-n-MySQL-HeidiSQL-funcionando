from django.contrib import admin
from django.urls import path
from moduloEmpleados import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', views.getListadoEmpleados, name="listado_empleados"),
    path('empleados/nuevo/', views.addEmpleado, name="add_empleado"),
    path('empleados/editar/<int:id>/', views.editEmpleado, name="edit_empleado"),
    path('empleados/eliminar/<int:id>/', views.deleteEmpleado, name="delete_empleado"),
]