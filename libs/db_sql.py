#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 5:03 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : db_sql.py

import datetime
from flask_sqlalchemy import SQLAlchemy
from libs import config
from flask import Flask
from libs.mainFun import class_to_dict

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

# db = SQLAlchemy()

# 表设计
class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)


class Targets(db.Model):
    __tablename__ = 'targets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    site = db.Column(db.String(255), unique=True)
    scan_code = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)


# 所有数据库调用方法

# 查询扫描任务 分页
def query_site_list(query='', pageNm=1, pageSize=5):
    # 限制limit 防止拒绝服务
    if pageSize < 500:
        index = (pageNm - 1) * pageSize
        total = db.session.query(Targets).filter(Targets.id).count()
        targetlist = db.session.query(Targets).filter(Targets.site.like('%'+query+'%')).limit(pageSize).offset(index).all()
        return class_to_dict(targetlist)


# 插入扫描任务
def add_site(site, scan_code):
    sites = Targets(site=site, scan_code=scan_code)
    db.session.add(sites)
    db.session.commit()

