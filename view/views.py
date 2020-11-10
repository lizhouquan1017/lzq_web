# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/9 下午2:48
@Auth ： lizhouquan
@File ：views.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from utils import sqlhelp
from django.shortcuts import render, redirect, HttpResponse
import json


def classes(request):
    class_list = sqlhelp.get_list('select id, title from class', [])
    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sqlhelp.modify('insert into class(title) values(%s)', [title, ])
        return HttpResponse('ok')
    else:
        return HttpResponse('班级标题不能为空')


def edit_class(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('id')
        title = request.POST.get('title')
        sqlhelp.modify('update class set title=%s where id=%s', [title, nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = "处理异常"

    return HttpResponse(json.dumps(ret))


def del_class(request):
    nid = request.GET.get('nid')
    sqlhelp.modify('delete from class where id=%s', [nid, ])
    return redirect('/classes/')
