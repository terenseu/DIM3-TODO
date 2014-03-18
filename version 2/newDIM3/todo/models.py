from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=64)
    group_member = models.ManyToManyField(User)

class List(models.Model):
    list_name = models.CharField(max_length=64)
    group = models.ForeignKey(Group, blank=True,  null=True)
    # not sure if can FK to user
    owner = models.ForeignKey(User)

class Task(models.Model):
    list = models.ForeignKey(List)
    task_name = models.CharField(max_length=64)
    url = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_due = models.DateField(blank=True,null=True)
    done = models.BooleanField(default=False)
    created_by = models.CharField(max_length=32)
    assigned_to = models.CharField(max_length=32, blank=True, null=True)
    message = models.TextField(blank=True,  null=True)

    #def __unicode__(self):
    #    return self.name

