#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 6:28 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : ceshi.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from libs import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)

username = 'admin1'
password = '96e79218965eb72c92a549dd5a330112'

data = db.session.query(Users).filter(Users.username == username).filter(Users.password == password).first()
print(data)
if data:
    print("succ")
else:
    print("no")