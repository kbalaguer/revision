from  django import forms

class CrearGatoForm(forms.Form):
    nombre=forms.CharField(max_length=10)
    edad=forms.IntegerField()
    fecha_nacimiento=forms.DateField(required=False)