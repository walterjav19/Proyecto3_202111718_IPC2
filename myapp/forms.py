
from django import forms

class CreateNewTask(forms.Form):
    title=forms.CharField(label="Titulo Tarea",max_length=200)
    description=forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name=forms.CharField(label="Nombre",max_length=200)    