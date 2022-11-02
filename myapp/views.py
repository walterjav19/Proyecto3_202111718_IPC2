from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .expresiones import verificar_fecha,generar_numero

from .recursos_configuracion import Configuracion_Recurso

from .configuracion import Configuracion

from .categoria import Categoria

from .instancia import Instancia

from .cliente import Cliente

from .recurso import Recurso
from django.contrib import messages
from .leer_xml import Leer,lista_objetos_clientes,lista_objetos_categoria,lista_objetos_recursos,listado_objetos_consumo
import webbrowser as wb
from .models import Project,Task
from django.shortcuts import get_object_or_404,render,redirect
from .forms import Crear_Cliente, CreateNewProject, CreateNewTask,Enviar_Mensaje, Enviar_Mensaje_consumo,Crear_recurso,Crear_Instancias,Crear_Categorias,Crear_Configs,Crear_recursos_config,Facturacion



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
final_date=""
consumos_rango_fechas=[]
def proceso_facturacion(request):
    if request.method== 'GET':
        return render(request,"proceso_facturacion.html",{
            'form':Facturacion()
        })
    else:
        global consumos_rango_fechas,final_date
        consumos_rango_fechas=[]
        start_month=request.POST['start_date_month']
        start_day=request.POST['start_date_day']
        start_year=request.POST['start_date_year']
        start_date=f'{start_day}/{start_month}/{start_year}'
        final_month=request.POST['end_date_month']
        final_day=request.POST['end_date_day']
        final_year=request.POST['end_date_year']
        final_date=f'{final_day}/{final_month}/{final_year}'
        print(start_date+" -> "+final_date)
        i=0        
        for consumo in listado_objetos_consumo:
            if verificar_fecha(start_date,final_date,consumo.fecha)==True:
                consumos_rango_fechas.append(consumo)
                corr=generar_numero()
                consumo.set_n_factura(corr)
                consumo.set_n(i)
                i+=1
            else:
                pass    
        return redirect('c_facturas')




def mostrar_clientes_facturar(request):
    global consumos_rango_fechas
    if request.method== 'GET':
        return render(request,"facturas.html",{
        'facturas':consumos_rango_fechas
        })
    
def mostrar_factura_individual(request,num):
    return render(request,"factura.html",{
        'factura':consumos_rango_fechas[num],
        'f_date': final_date
    })


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

def mostrar_instancias(request,num):
    return render(request,"instancias.html",{
        'instancias': lista_objetos_clientes[num].lista_instancias
    })

def mostrar_categorias(request):
    return render(request,"categorias.html",{
        'categorias': lista_objetos_categoria
    })
lista_dentro_categoria=[]
def mostrar_configuraciones(request,num):
    global lista_dentro_categoria
    lista_dentro_categoria=lista_objetos_categoria[num].lista_configuraciones
    return render(request,"configuraciones.html",{
        'configuraciones': lista_objetos_categoria[num].lista_configuraciones
    })
    

def mostrar_configuraciones_recursos(request,num):
    return render(request,"recursos_config.html",{
        'recursos': lista_dentro_categoria[num].lista_recursos
    })

def creacion_datos(request):
    return render(request,"creacion_datos.html")


def create_recurso(request):
    if request.method== 'GET':
        return render(request,'crear_recurso.html',{
        'form': Crear_recurso()
    })
    else:
        id=request.POST['id']
        nombre=request.POST['nombre']
        abreviatura=request.POST['abreviatura']
        metrica=request.POST['metrica']
        tipo=request.POST['tipo']
        valor=request.POST['valor']
        if tipo=='1':
            tipo="Hardware"
        else:
            tipo="Software"   
        objeto_recurso=Recurso(id,nombre,abreviatura,metrica,tipo,valor)
        lista_objetos_recursos.append(objeto_recurso)
        messages.success(request,"Revise sus recursos")
        return redirect('Crear_Recurso')

nit_c=""
nombre_c=""
usuario_c=""
clave_c=""
direccion_c=""
correo_c=""
objt_cli=None
lista_parametro=[]

def create_cliente(request):
    global nit_c,nombre_c,usuario_c,clave_c,direccion_c,correo_c,objt_cli,lista_parametro
    lista_parametro=[]
    if request.method== 'GET':
        return render(request,'crear_clientes.html',{
        'form': Crear_Cliente()
    })
    else:
        nit_c=request.POST['nit']
        nombre_c=request.POST['nombre']
        usuario_c=request.POST['usuario']
        clave_c=request.POST['clave']
        direccion_c=request.POST['direccion']
        correo_c=request.POST['correo']
        if lista_objetos_clientes==[]:
            objt_cli=Cliente(nit_c,nombre_c,usuario_c,clave_c,direccion_c,correo_c,None,0)
            lista_objetos_clientes.append(objt_cli)
        else:
            tamanio_lista=len(lista_objetos_clientes)
            objt_cli=Cliente(nit_c,nombre_c,usuario_c,clave_c,direccion_c,correo_c,None,tamanio_lista)
            lista_objetos_clientes.append(objt_cli)
            

        messages.success(request,"Verifique las instancias que quiere crear para este cliente")
        return redirect('Crear_Instancias')

def create_instancias(request):
    global nit_c,nombre_c,usuario_c,clave_c,direccion_c,correo_c,objt_cli,lista_parametro
    
    if request.method== 'GET':
        return render(request,'crear_instancias.html',{
        'form': Crear_Instancias(),
        'nombre': nombre_c
    })
    else:
        id_instancia=request.POST['id']
        id_Configuracion=request.POST['id_config']
        nombre=request.POST['nombre']
        fecha_Inicio=request.POST['fecha_inicio']
        estado=request.POST['estado']
        Fecha_Final=request.POST['fecha_final']
        if estado=='1':
            estado="Vigente"
            Fecha_Final="N/A"
        else:
            estado="Cancelada"    
        
        objt_instancia=Instancia(id_instancia,id_Configuracion,nombre,fecha_Inicio,estado,Fecha_Final)
        lista_parametro.append(objt_instancia)
        objt_cli.set_lista_instancias(lista_parametro)
        messages.success(request,"Revise sus Clientes e instancias")
        return redirect('Crear_Instancias')

objt_cate=None
lista_parametro_configs=[]
n_configur=0
def create_categorias(request):
    global objt_cate,lista_parametro_configs,n_configur
    lista_parametro_configs=[]
    n_configur=0
    if request.method== 'GET':
        return render(request,'crear_categorias.html',{
        'form': Crear_Categorias()
    })
    else:
        id_cate=request.POST['id']
        nombre_cate=request.POST['nombre']
        descripcion_cate=request.POST['descripcion']
        c_trabajo=request.POST['carga_trabajo']
        if lista_objetos_categoria==[]:
            objt_cate=Categoria(id_cate,nombre_cate,descripcion_cate,c_trabajo,None,0)
        else:
            objt_cate=Categoria(id_cate,nombre_cate,descripcion_cate,c_trabajo,None,len(lista_objetos_categoria))
        lista_objetos_categoria.append(objt_cate)         
        messages.success(request,"asigne configuraciones ")
        return redirect('Crear_Configuraciones')

objt_Config=None
lista_parametro_recu=[]
def create_configs(request):
    global objt_cate,objt_Config,lista_parametro_configs,n_configur,lista_parametro_recu
    lista_parametro_recu=[]
    if request.method== 'GET':
        return render(request,'crear_configuraciones.html',{
        'form': Crear_Configs()
    })
    else:
        id_config=request.POST['id']
        nombre_config=request.POST['nombre']
        descripcion_config=request.POST['descripcion']
        objt_Config=Configuracion(id_config,nombre_config,descripcion_config,None,n_configur)
        lista_parametro_configs.append(objt_Config)
        objt_cate.set_lista_configuraciones(lista_parametro_configs)
        n_configur+=1
        messages.success(request,"asigne recursos")
        return redirect('Crear_Recurso_Config')

def create_Recursos_Configuraciones(request):
    global objt_Config,lista_parametro_recu
    if request.method== 'GET':
        return render(request,'crear_recurso_config.html',{
        'form': Crear_recursos_config()
    })
    else:
        id_recur=request.POST['id']
        cantidad=request.POST['cantidad']
        objt=Configuracion_Recurso(id_recur,cantidad)
        lista_parametro_recu.append(objt)
        objt_Config.set_lista_recursos(lista_parametro_recu)
        #print(id_recur,cantidad)
        messages.success(request,"asigne mas recursos")
        return redirect('Crear_Recurso_Config')



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

