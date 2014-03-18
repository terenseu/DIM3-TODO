from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404

from todo.models import List, Task, Group
from todo.form import RegistrationForm, ListForm, TaskForm

# Create your views here.

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


        return render_to_response('loggedin.html', {'username': request.user.username})

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

def add_list(request):
    if request.POST:
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.owner = request.user
            list.save()
            #form.save()
            return HttpResponseRedirect('/index/')
    else:
        form = ListForm()

        args = {}
        args.update(csrf(request))
        args['form'] = form

        return render_to_response('add_list.html', args)

def list(request, list_id, list_name_url):
    context = RequestContext(request)
    list_name = list_name_url.replace('_', ' ')
    context_dict = {'list_id':list_id, 'list_name':list_name}

    try:
        list = List.objects.get(list_name=list_name)
        list.url = list_name
        tasks = Task.objects.filter(list=list)
        context_dict['tasks'] = tasks
        context_dict['list'] = list
    except List.DoesNotExist:
        pass



    return render_to_response('list.html', context_dict, context)

def index(request):
    if request.user.is_authenticated():
        context = RequestContext(request)
        list_list = List.objects.filter(owner=request.user)
        context_dict = {'lists':list_list}
        for list in list_list:
            list.url = list.list_name.replace(' ', '_')
            list.id = list.id
        return render_to_response('index.html', context_dict, context)
        #return render_to_response('index.html', {'lists' : List.objects.filter(owner=request.user)})
    else:
        return HttpResponseRedirect('/accounts/login')

def add_task(request, list_name_url):
    #list.url = list_name_url
    context = RequestContext(request)
    list_name = list_name_url.replace('_', ' ')
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.list = List.objects.get(list_name=list_name)
            task.created_by = request.user
            task.save()
    else:
        form = TaskForm()

        args = {}
        args.update(csrf(request))
        args['form'] = form

        return render_to_response('add_task.html', args)

#    if request.POST:
#        form = TaskForm(request.POST)
#        if form.is_valid():
#            task = form.save(commit=False)
#            # pass list_name here, but how
#            task.created_by = request.user
#            task.save()
#            #form.save()
#            #return HttpResponseRedirect('/index/')
#            return render_to_response('add_task.html')
#    else:
#        form = TaskForm()
#
#        args = {}
#        args.update(csrf(request))
#        args['form'] = form
#
#        return render_to_response('add_task.html', args)