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
    path('mostrar_clientes/',views.mostrar_clientes,name="clientes")
]