from django.contrib import admin
from todo.models import List
from todo.models import Task
from todo.models import Group


# Register your models here.
admin.site.register(Task)
admin.site.register(List)
admin.site.register(Group)

