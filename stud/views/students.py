# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse

#views 4 stud
def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Ігор',
         'last_name': u'Горобець',
         'ticket': 700,
         'image': 'img/tweat.jpg'},
        {'id': 2,
         'first_name': u'Ігор',
         'last_name': u'Семенюк',
         'ticket': 777,
         'image': 'img/sem.png'},
        {'id': 3,
         'first_name': u'Совпадєніє?',
         'last_name': u'Не думаю',
         'ticket': 707,
         'image': 'img/kfc.jpg'},
    )
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)