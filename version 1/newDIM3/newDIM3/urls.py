from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newDIM3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^test/$' , 'todo.views.test'),
    url(r'^test_template/$', 'todo.views.test_template'),
    url(r'^test_template_easy/$', 'todo.views.test_template_easy'),
    url(r'^tasks/$', 'todo.views.tasks'),

    # admin url
    url(r'^admin/', include(admin.site.urls)),

    #Create Task url
    url(r'^create/$' , 'todo.views.create'),

    #user auth urls
    url(r'index/' , 'todo.views.login'),
    url(r'^accounts/login/$' , 'todo.views.login'),
    url(r'^accounts/auth/$' , 'todo.views.auth_view'),
    url(r'^accounts/logout/$' , 'todo.views.logout'),
    url(r'^accounts/loggedin/$' , 'todo.views.loggedin'),
    url(r'^accounts/invalid/$' , 'todo.views.invalid_login'),
    url(r'^accounts/register/$' , 'todo.views.register_user'),
    url(r'^accounts/register_success/$' , 'todo.views.register_success'),
)
