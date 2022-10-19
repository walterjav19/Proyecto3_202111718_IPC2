from email.policy import default
from turtle import title
from django.db import models

# Create your models here.

class Project(models.Model):#hereda los modelos que django ya trae
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.title+'-'+self.project.name


        