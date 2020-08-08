from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Project(models.Model):
    project_name = models.CharField(max_length = 256)
    #project_description = name = models.TextField()


class Entry(models.Model):
    task = models.CharField(max_length = 256)
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
           

    
    







