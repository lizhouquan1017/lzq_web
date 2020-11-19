# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/9 下午2:49
@Auth ： lizhouquan
@File ：sqlhelp.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import pymysql


class SqlHelp(object):

    def __init__(self):
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3309, user='root', passwd='123456', db='sts', charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchall()
        return result

    def get_one(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    def modify(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def multiple_modify(self, sql, args):
        self.cursor.executemany(sql, args)
        self.conn.commit()

    def create(self, sql, args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid

    def close(self):
        self.cursor.close()
        self.conn.close()
