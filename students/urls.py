# -*- coding: utf-8 -*-



from django.conf.urls import url
from django.contrib import admin
import stud.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', stud.views.students_list, name='home'),
]
