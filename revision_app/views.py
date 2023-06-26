from django.shortcuts import render
from django.http import HttpResponse
from revision_app.forms import CrearGatoForm
from revision_app.models import GatoModel

# Create your views here.

def inicio(request):
    return render(request,'htmls/inicio.html')

def crear_gato(request):
    mensaje=''
    if request.method=='POST':
        form=CrearGatoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            gato=GatoModel(nombre=info['nombre'],edad=info['edad'],fecha_nacimiento=info['fecha_nacimiento']) 
            gato.save()
            form=CrearGatoForm()
            mensaje=f'se creo el gato :{gato.nombre}'
        else:
            return render(request,'htmls/crear_gato.html',{'formulario':form})
    
    form=CrearGatoForm()
    return render(request, 'htmls/crear_gato.html',{'formulario':form,'mensaje':mensaje})