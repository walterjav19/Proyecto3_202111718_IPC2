

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

class Crear_recurso(forms.Form):
    id=forms.CharField(label="id",max_length=200)
    nombre=forms.CharField(label="Nombre",max_length=200)
    abreviatura=forms.CharField(label="Abreviatura",max_length=200)
    metrica=forms.CharField(label="Metrica",max_length=200)
    tipo=forms.CharField(label="Tipo",max_length=200)
    valor=forms.FloatField(label="Valor X Hora")    
    
class Crear_Cliente(forms.Form):
       nit=forms.CharField(label="Nit",max_length=200)
       nombre=forms.CharField(label="Nombre",max_length=200)
       usuario=forms.CharField(label="Usuario",max_length=200)
       clave=forms.CharField(label="Clave",max_length=200)
       direccion=forms.CharField(label="Direccion",max_length=200)
       correo=forms.CharField(label="Correo Electronico",max_length=200)

class Crear_Instancias(forms.Form):
       id=forms.CharField(label="Id Instancia",max_length=200)
       id_config=forms.CharField(label="Id Configuracion",max_length=200)
       nombre=forms.CharField(label="nombre",max_length=200)
       fecha_inicio=forms.DateField(label="Fecha Inicio")
       estado=forms.ChoiceField(label="estado",choices=[('1', 'Activo'), ('2', 'Inactivo')])
       fecha_final=forms.DateField(label="Fecha Final")
       
class Crear_Categorias(forms.Form):
       id=forms.CharField(label="Id Categoria",max_length=200)
       nombre=forms.CharField(label="nombre",max_length=200)
       descripcion=forms.CharField(label="Descripcion de la categoria",widget=forms.Textarea)
       carga_trabajo=forms.CharField(label="carga de trabajo",max_length=200)

class Crear_Configs(forms.Form):
       id=forms.CharField(label="Id Configuracion",max_length=200)
       nombre=forms.CharField(label="nombre",max_length=200)
       descripcion=forms.CharField(label="Descripcion de la configuracion",widget=forms.Textarea)

class Crear_recursos_config(forms.Form):
       id=forms.CharField(label="Id del recurso",max_length=200)
       cantidad=forms.CharField(label="cantidad del recurso",max_length=200)
        
    