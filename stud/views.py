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

#Views 4 groups
def groups_list(request):
    groups = (
        {'id': 1,
         'group_name': u'TK-91',
         'leader_name': u'Горобець Ігор'},
        {'id': 2,
         'group_name': u'KT-19',
         'leader_name': u'Семенюк Ігор'},
        {'id': 3,
         'group_name': u'T9-K1',
         'leader_name': u'Совпадєніє? Не думаю'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)