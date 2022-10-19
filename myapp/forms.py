
from django import forms

class CreateNewTask(forms.Form):
    title=forms.CharField(label="Titulo Tarea",max_length=200)
    description=forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name=forms.CharField(label="Nombre",max_length=200)    


class Enviar_Mensaje(forms.Form):
    mensaje_configuracion=forms.CharField(label="Coloque aqui la ruta del XML")


class Enviar_Mensaje_consumo(forms.Form):
    mensaje_consumo=forms.CharField(label="Coloque aqui la ruta del XML de consumo")