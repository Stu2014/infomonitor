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

