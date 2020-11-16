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
    ret = {'status': True, 'message': None}
    try:
        title = request.POST.get('title')
        if len(title) > 0:
            sqlhelp.modify('insert into class(title) values(%s)', [title, ])
        else:
            print('名字为空')
            ret['status'] = False
            ret['message'] = '班级名称为空'
    except Exception as e:
        ret['status'] = False
        ret['message'] = '处理异常'

    return HttpResponse(json.dumps(ret))


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


def student(request):
    student_list = sqlhelp.get_list("select student.id,student.name,student.class_id,class.title "
                                    "from student left JOIN class on student.class_id = class.id", [])
    class_list = sqlhelp.get_list('select id, title from class', [])
    return render(request, 'student.html', {'student_list': student_list, 'class_list': class_list})


def add_student(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        print(name)
        print(class_id)
        if len(name) > 0:
            sqlhelp.modify('insert into student(name, class_id) values(%s, %s)', [name, class_id])
        else:
            print('名字为空')
            ret['status'] = False
            ret['message'] = '名字为空'
    except Exception as e:
        ret['status'] = False
        ret['message'] = '处理异常'

    return HttpResponse(json.dumps(ret))


def del_student(request):
    nid = request.GET.get('nid')
    sqlhelp.modify('delete from student where id=%s', [nid, ])
    return redirect('/student/')


def teachers(request):
    teacher_list = sqlhelp.get_list("""select teacher.id as tid,teacher.name,class.title from teacher
                                        LEFT JOIN teacher2class on teacher.id = teacher2class.t_id
                                        left JOIN class on class.id = teacher2class.c_id;""", [])
    result = {}
    for row in teacher_list:
        tid = row['tid']
        if tid in result:
            result[tid]['title'].append(row['title'])
        else:
            result[tid] = {'tid': row['tid'], 'name': row['name'], 'title': [row['title']]}

    class_list = sqlhelp.get_list('select id, title from class', [])

    return render(request, 'teachers.html', {'teacher_list': result.values(), 'class_list': class_list})


def add_teacher(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        if len(name) > 0:
            sqlhelp.modify('insert into teacher(name) values(%s)', [name, ])
            tid = sqlhelp.get_one('select id from teacher where name = %s', [name, ])
            sqlhelp.modify('insert into teacher2class(t_id, c_id) values (%s, %s)', [tid['id'], class_id])
        else:
            ret['status'] = False
            ret['message'] = '名字为空'
    except Exception as e:
        ret['status'] = False
        ret['message'] = '处理异常'



    return HttpResponse(json.dumps(ret))

















