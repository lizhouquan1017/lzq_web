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
import json, pymysql


def classes(request):
    class_list = sqlhelp.get_list('select id, title from class', [])
    print(class_list)
    return render(request, 'classes.html', {'class_list': class_list})


def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        result = sqlhelp.get_one('select id,title from class where id = %s', [nid])
        return render(request, 'edit_class.html', {'result': result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')
        sqlhelp.modify('update class set title=%s where id=%s', [title, nid, ])
        return redirect('/classes/')


def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        class_name = request.POST.get('title')
        if len(class_name) > 0:
            sqlhelp.modify('insert into class(title) values(%s)', [class_name, ])
            return redirect('/classes/')
        else:
            return render(request, 'add_class.html', {'msg': '班级名称不能为空'})
