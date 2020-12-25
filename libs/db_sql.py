#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 5:03 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : db_sql.py

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)

# 查询扫描任务 分页
def query_site_list(query='', pageNm=1, pageSize=10):
    if pageSize < 500:
        index = (pageNm - 1) * pageSize
        db.query(Sites.)