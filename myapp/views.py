from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .leer_xml import Leer,lista_objetos_clientes,lista_objetos_categoria,lista_objetos_recursos,listado_objetos_consumo
import webbrowser as wb
from .models import Project,Task
from django.shortcuts import get_object_or_404,render,redirect
from .forms import CreateNewProject, CreateNewTask,Enviar_Mensaje, Enviar_Mensaje_consumo



# Create your views here.
def hello(request,username):
    print(username)
    return HttpResponse("<h2>Hola amigo %s</h2>"%username)


interprete=Leer()
def index(request):
    if request.method== 'GET':
        return render(request,'index.html',{
        'form':Enviar_Mensaje()
        })   
    else:    
        print(request.POST['mensaje_configuracion'])
        path=request.POST['mensaje_configuracion']
        interprete.leer_xml_objetos(path)
        return redirect('me1')

def mensaje_configuracion_exitoso(request):
    return render(request,'notificacion.html',{
        'lista_recursos':lista_objetos_recursos,
        'lista_categorias':lista_objetos_categoria,
        'lista_clientes': lista_objetos_clientes,
        'n_cli':interprete.clientes_nuevos,
        'n_r':interprete.recursos_nuevos,
        'n_ca':interprete.categorias_nuevas
    })


def about(request):
    if request.method== 'GET':
        return render(request,'about.html') 
    else:
        #cuando exista el archivo pdf poner la ruta recordar
        #wb.open_new("")
        return redirect("about")

def consumo(request):
    if request.method== 'GET':
        return render(request,'consumo.html',{
        'form':Enviar_Mensaje_consumo()
        })
    else:
        path=request.POST['mensaje_consumo']
        interprete.leer_consumo(path)
        return redirect('me2')     
        
def mensaje_consumo(request):
    return render(request,'notificacion_consumo.html',{
        'lista_consumo': listado_objetos_consumo,
        'nuevos_consumo': interprete.consumos_nuevos
    })

def operaciones_sistema(request):
    return render(request,"operaciones_sistema.html")

def datos(request):
    return render(request,"datos.html")

def mostrar_recursos(request):
    return render(request,"recursos.html",{
        'recursos':lista_objetos_recursos
    })

def mostrar_clientes(request):
    return render(request,"clientes.html",{
        'clientes': lista_objetos_clientes
    })



def task(request):
    #task=get_object_or_404(Task,id=id)
    tasks=Task.objects.all()
    return render(request,'tasks.html',{
        'tasks': tasks
    })       

def create_task(request):
    #print(request.GET['title'])
    #print(request.GET['description'])
    if request.method== 'GET':
        return render(request,'create_tasks.html',{
        'form': CreateNewTask()
    })
    else:    
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'], 
        project_id=2)
        return redirect('tasks')


def create_projects(request):
    if request.method== 'GET':
        return render(request,'create_project.html',{
        'form': CreateNewProject()
    })
    else:    
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

