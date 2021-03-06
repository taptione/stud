from django.conf.urls import url
from django.contrib import admin
from stud.views import students, groups, contact_admin
from .settings import MEDIA_ROOT, DEBUG
from django.views.static import serve
urlpatterns = [
    url(r'^admin/', admin.site.urls),

#stud urls
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', students.students_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students.students_edit, name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students.students_delete, name='students_delete'),


#group urls
    url(r'^groups/$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', groups.groups_add, name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups.groups_edit, name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups.groups_delete, name='groups_delete'),

#contact admin form
    url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),
]
# serve files from media folder
if DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    ]