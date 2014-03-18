from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^main/$','todo.views.main'),
    url(r'^index/$', 'todo.views.index'),
    url(r'^add_list/$', 'todo.views.add_list'),
    #url(r'^list/(?P<list_name_url>\w+)/$', views.list, name='list'),
    url(r'^(?P<list_id>(\d+))/(?P<list_name_url>\w+)/$', views.list, name='list'),
    url(r'^(?P<list_id>(\d+))/(?P<list_name_url>\w+)/add_task/$', views.add_task, name='add_task'),


    #user auth urls
    url(r'^$' , 'todo.views.login'),
    url(r'^accounts/login/$' , 'todo.views.login'),
    url(r'^accounts/auth/$' , 'todo.views.auth_view'),
    url(r'^accounts/logout/$' , 'todo.views.logout'),
    url(r'^accounts/loggedin/$' , 'todo.views.loggedin'),
    url(r'^accounts/invalid/$' , 'todo.views.invalid_login'),
    url(r'^accounts/register/$' , 'todo.views.register_user'),
    url(r'^accounts/register_success/$' , 'todo.views.register_success'),


    url(r'^admin/', include(admin.site.urls))
)
