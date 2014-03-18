from django.shortcuts import render_to_response
from todo.models import Task
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from todo.form import RegistrationForm
from todo.form import TaskForm
from django.shortcuts import get_object_or_404


# Create your views here.

def tasks(request):
    #task = get_object_or_404(Task, user=request.user)
    #task_user = Task.objects.get(user=request.user)


    if request.user.is_authenticated():
        return render_to_response('tasks.html' , {'tasks' : Task.objects.filter(user=request.user)})
    else:
        return HttpResponseRedirect('/accounts/login')

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username' , '')
    password = request.POST.get('password' , '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    if request.user.is_authenticated():
        return render_to_response('loggedin.html' , {'username': request.user.username})

    else:
        return HttpResponseRedirect('/accounts/login')

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = RegistrationForm()
    print(args)
    return render_to_response('register.html', args)


def register_success(request):
    return render_to_response('register_success.html')

def create(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            #form.save()
            task = form.save(commit=False)
            task.user = request.user
            task.save()

            return HttpResponseRedirect('/tasks/')

    else:
        form = TaskForm()

        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('new_task.html' , args)
