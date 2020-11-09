# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/9 下午2:49
@Auth ： lizhouquan
@File ：sqlhelp.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import pymysql


def get_one(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='root', passwd='123456', db='sts', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def get_list(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='root', passwd='123456', db='sts', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def modify(sql, args):
    conn = pymysql.connect(host='127.0.0.1', port=3309, user='root', passwd='123456', db='sts', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()
