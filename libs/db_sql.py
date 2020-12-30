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
from libs.log import logger
from libs.main import class_to_dict

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# db = SQLAlchemy()

# 表设计
# 用户表
class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)


# 添加网站目标表
class Targets(db.Model):
    __tablename__ = 'targets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    site = db.Column(db.String(255), unique=True)
    scan_code = db.Column(db.Integer)
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)


# 存js表
class Jsu(db.Model):
    __tablename__ = 'jsu'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    target = db.Column(db.String(2000))
    jsu = db.Column(db.String(2000))
    ctime = db.Column(db.DateTime, default=datetime.datetime.now)


# 所有数据库调用方法

# 查询扫描任务 分页
def query_site_list(query='', pageNm=1, pageSize=5):
    # 限制limit 防止拒绝服务
    try:
        if pageSize < 500:
            index = (pageNm - 1) * pageSize
            total = db.session.query(Targets).filter(Targets.id).count()
            targetlist = db.session.query(Targets).filter(Targets.site.like('%' + query + '%')).limit(pageSize).offset(
                index).all()
            data = {}
            data['total'] = total
            data['targetlist'] = class_to_dict(targetlist)
            return data
    except Exception as e:
        db.session.rollback()
        logger.info("query_site_list error,{}".format(e))



# 查询js 分页
def query_js_list(query='', pageNm=1, pageSize=5):
    # 限制limit 防止拒绝服务
    try:
        if pageSize < 500:
            index = (pageNm - 1) * pageSize
            total = db.session.query(Jsu).filter(Jsu.id).count()
            targetlist = db.session.query(Jsu).filter(Jsu.target.like('%' + query + '%')| \
                                                      Jsu.jsu.like('%' + query + '%')
                                                      ).limit(pageSize).offset(
                index).all()
            data = {}
            data['total'] = total
            data['targetlist'] = class_to_dict(targetlist)
            return data
    except Exception as e:
        db.session.rollback()
        logger.info("query_js_list error,{}".format(e))


# 插入扫描任务
def add_site(site, scan_code):
    try:
        sites = Targets(site=site, scan_code=scan_code)
        db.session.add(sites)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        logger.info("add_site error,{}".format(e))


# 更改扫描任务状态
def update_site(site, scan_code):
    try:
        db.session.query(Targets).filter(Targets.site == site).update({Targets.scan_code : scan_code})
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        logger.info("update_site error,{}".format(e))


# 插入js url
def add_js(site, jsurl):
    try:
        urls = Jsu(target=site, jsu=jsurl)
        db.session.add(urls)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        logger.info("add_js error,{}".format(e))


