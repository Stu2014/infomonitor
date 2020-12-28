#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 6:28 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : ceshi.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from libs import config
import datetime

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)

class Targets(db.Model):
    __tablename__ = 'targets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    site = db.Column(db.String(255))
    scan_code = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)


username = 'admin1'
password = '96e79218965eb72c92a549dd5a330112'

# data = db.session.query(Users).filter(Users.username == username).filter(Users.password == password).first()
# print(data)
# if data:
#     print("succ")
# else:
#     print("no")

# aa = 'http://baidu.coms/s'
# bb = 0
# aaa = Targets(site=aa, scan_code=bb)
#
# db.session.add(aaa)
# db.session.commit()
def class_to_dict(obj):
    is_list = obj.__class__ == [].__class__
    is_set = obj.__class__ == set().__class__
    if is_list or is_set:
        obj_arr = []
        for o in obj:
            dict = {}
            a = o.__dict__
            if "_sa_instance_state" in a:
                del a['_sa_instance_state']
            dict.update(a)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        a = obj.__dict__
        if "_sa_instance_state" in a:
            del a['_sa_instance_state']
        dict.update(a)

query=''
pageSize=5
pageNm=1
index = (pageNm - 1) * pageSize
targetlist = db.session.query(Targets).filter(Targets.site.like('%' + query + '%')).limit(pageSize).offset(index).all()
print(class_to_dict(targetlist))

data = []
# for line in targetlist:
#     data.append({"id": line[0], "site": line[1], "scan_code": line[2], "ctime": line[3]})
print(data)
# user_obj=Targets.query.filter(Targets.site.like('%'+query+'%')).paginate(index, pageSize,False)
# #遍历时要加上items
# object_list =user_obj.items
# print(object_list)
# data = []
# for line in object_list:
#     print(line[0])
#     # data.append({"id": line[0], "site": line[1], "scan_code": line[2], "ctime": line[3]})
# print(data)