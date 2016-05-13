from django.conf.urls import url
from django.contrib import admin
import stud.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),

#stud urls
    url(r'^$', stud.views.students_list, name='home'),
    url(r'^students/add/$', stud.views.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', stud.views.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', stud.views.students_delete, name='students_delete'),

#group urls
    url(r'^groups/$', stud.views.groups_list, name='groups'),
    url(r'^groups/add/$', stud.views.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', stud.views.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', stud.views.groups_delete, name='groups_delete'),
]
