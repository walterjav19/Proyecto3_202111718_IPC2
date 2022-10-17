#from django.shortcuts import render
from turtle import title
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render,redirect
from .forms import CreateNewProject, CreateNewTask
# Create your views here.
def hello(request,username):
    print(username)
    return HttpResponse("<h2>Hola amigo %s</h2>"%username)



def index(request):
    title='Welcome to Django Course!!'
    return render(request,'index.html',{
        'title':title
    })   

def about(request):
    username='fazt'
    return render(request,'about.html',{
        'username':username
    }) 

def projects(request):
    #Lista_proyectos=list(Project.objects.values())
    projects=Project.objects.all()
    return render(request,'projects.html',{
        'projects':projects
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
