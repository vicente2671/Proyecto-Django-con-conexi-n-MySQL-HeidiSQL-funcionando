from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Leer (Listado)
def getListadoEmpleados(request):
    empleados = Employee.objects.all()
    return render(request, "listadoEmpleados.html", {"empleados": empleados})

# Crear
def addEmpleado(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_empleados')
    else:
        form = EmployeeForm()
    return render(request, "addEmpleado.html", {"form": form})

# Actualizar
def editEmpleado(request, id):
    empleado = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listado_empleados')
    else:
        form = EmployeeForm(instance=empleado)
    return render(request, "editEmpleado.html", {"form": form})

# Eliminar
def deleteEmpleado(request, id):
    empleado = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        empleado.delete()
        return redirect('listado_empleados')
    return render(request, "deleteEmpleado.html", {"empleado": empleado})
