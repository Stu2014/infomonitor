#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 5:47 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : config.py

mysql_user = 'root'
mysql_password = 'root'
mysq_host = '127.0.0.1'
mysql_port = '3306'
mysql_db = 'infom'

cnnnect = "mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8".format(mysql_user, mysql_password, mysq_host, mysql_port, mysql_db)
# print(cnnnect)
SQLALCHEMY_DATABASE_URI = cnnnect
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

