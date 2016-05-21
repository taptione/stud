# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.http import HttpResponse

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