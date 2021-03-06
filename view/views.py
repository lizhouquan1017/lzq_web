# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/9 下午2:48
@Auth ： lizhouquan
@File ：views.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

from datetime import timedelta
from utils.sqlhelp import SqlHelp
from django.shortcuts import render, redirect, HttpResponse
import json
import datetime


def classes(request):
    tk = request.COOKIES.get('ticket')
    if not tk:
        return redirect('/login')
    else:
        obj = SqlHelp()
        class_list = obj.get_list('select id, title from class', [])
        obj.close()
        return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    obj = SqlHelp()
    ret = {'status': True, 'message': None}
    try:
        title = request.POST.get('title')
        if len(title) > 0:
            obj.create('insert into class(title) values(%s)', [title, ])
            obj.close()
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
    obj = SqlHelp()
    try:
        nid = request.POST.get('id')
        title = request.POST.get('title')
        obj.modify('update class set title=%s where id=%s', [title, nid, ])
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = "处理异常"

    return HttpResponse(json.dumps(ret))


def del_class(request):
    obj = SqlHelp()
    nid = request.GET.get('nid')
    obj.modify('delete from class where id=%s', [nid, ])
    obj.close()
    return redirect('/classes/')


def student(request):
    obj = SqlHelp()
    student_list = obj.get_list("select student.id,student.name,student.class_id,class.title "
                                "from student left JOIN class on student.class_id = class.id", [])
    class_list = obj.get_list('select id, title from class', [])
    obj.close()
    return render(request, 'student.html', {'student_list': student_list, 'class_list': class_list})


def add_student(request):
    ret = {'status': True, 'message': None}
    obj = SqlHelp()
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        if len(name) > 0:
            obj.create('insert into student(name, class_id) values(%s, %s)', [name, class_id])
            obj.close()
        else:
            ret['status'] = False
            ret['message'] = '名字为空'
    except Exception as e:
        ret['status'] = False
        ret['message'] = '处理异常'

    return HttpResponse(json.dumps(ret))


def del_student(request):
    obj = SqlHelp()
    nid = request.GET.get('nid')
    obj.modify('delete from student where id=%s', [nid, ])
    obj.close()
    return redirect('/student/')


def teachers(request):
    obj = SqlHelp()
    teacher_list = obj.get_list("""select teacher.id as tid,teacher.name,class.title from teacher
                                        LEFT JOIN teacher2class on teacher.id = teacher2class.t_id
                                        left JOIN class on class.id = teacher2class.c_id;""", [])
    class_list = obj.get_list('select id, title from class', [])
    obj.close()
    result = {}
    for row in teacher_list:
        tid = row['tid']
        if tid in result:
            result[tid]['title'].append(row['title'])
        else:
            result[tid] = {'tid': row['tid'], 'name': row['name'], 'title': [row['title']]}

    return render(request, 'teachers.html', {'teacher_list': result.values(), 'class_list': class_list})


def add_teacher(request):
    obj = SqlHelp()
    if request.method == "GET":
        class_list = obj.get_list('select id,title from class', [])
        return render(request, 'add_teacher.html', {'class_list': class_list})
    else:
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        tid = obj.create('insert into teacher(name) values(%s)', [name])
        for cls_id in class_ids:
            obj.create('insert into teacher2class(t_id,c_id) values(%s,%s)', [tid, cls_id, ])
        obj.close()
        return redirect('/teachers/')


def edit_teacher(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = SqlHelp()
        teacher_info = obj.get_one('select id, name from teacher where id=%s', [nid, ])
        class_id_list = obj.get_list('select c_id from teacher2class where t_id=%s', [nid, ])
        class_list = obj.get_list('select id, title from class', [])
        temp = []
        for i in class_id_list:
            temp.append(i['c_id'])
        obj.close()
        print(teacher_info, class_id_list, class_list)
        return render(request, 'edit_teacher.html', {
            'teacher_info': teacher_info,
            'class_id_list': temp,
            'class_list': class_list,
        })
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        obj = SqlHelp()
        obj.modify('update teacher set name=%s where id=%s', [name, nid])
        obj.modify('delete from teacher2class where t_id=%s', [nid, ])
        for cls_id in class_ids:
            obj.modify('insert into teacher2class(t_id,c_id) values(%s,%s)', [nid, cls_id, ])
        obj.close()
        return redirect('/teachers/')


def get_all_class(request):
    obj = SqlHelp()
    class_list = obj.get_list('select id,title from class', [])
    obj.close()
    print(class_list)
    return HttpResponse(json.dumps(class_list))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        print(user)
        print(pwd)
        if user == 'lzq' and pwd == '123':
            obj = redirect('/classes')
            obj.set_cookie('ticket', 'abcdefg', max_age=10)
            return obj
        else:
            return render(request, 'login.html')








