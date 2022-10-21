from django.urls import path
from . import views
urlpatterns=[
    path('', views.index,name="index"),
    path('about/',views.about,name="about"),
    path('hello/<str:username>',views.hello,name="hello"),
    path('consumo/',views.consumo,name="consumo"),
    path('tasks/',views.task,name="tasks"),
    path('create_tasks/',views.create_task,name="create_tasks"),
    path('create_project/',views.create_projects,name="create_project"),
    path('mensaje_exito_1/',views.mensaje_configuracion_exitoso,name="me1"),
    path('mensaje_consumo/',views.mensaje_consumo,name="me2"),
    path('op_sistema/',views.operaciones_sistema,name="operaciones"),
    path('datos/',views.datos,name="datos"),
    path('mostrar_recursos/',views.mostrar_recursos,name="m_recursos"),
    path('mostrar_clientes/',views.mostrar_clientes,name="clientes"),
    path('mostrar_instancias/<int:num>',views.mostrar_instancias,name="intancias"),
    path('mostrar_categorias/',views.mostrar_categorias,name="categorias"),
    path('mostrar_configs/<int:num>',views.mostrar_configuraciones,name="configuraciones"),
    path('mostrar_recursos_configuraciones/<int:num>',views.mostrar_configuraciones_recursos,name="recursos_configs"),
    path('creacion_datos/',views.creacion_datos,name="creacion"),
    path('crear_recurso/',views.create_recurso,name="Crear_Recurso"),
    path('crear_cliente/',views.create_cliente,name="Crear_Cliente"),
    path('crear_instancias/',views.create_instancias,name="Crear_Instancias")
]