#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 11:33 上午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : jsinfo.py


import hashlib
from module import jsscan
from libs.log import logger
from libs.db_sql import *
from libs.db_sql import db
from libs.mainFun import *
from concurrent.futures import ThreadPoolExecutor
from flask import  request, Blueprint, session, redirect, url_for, render_template,make_response

executor = ThreadPoolExecutor(2)

user = Blueprint('user', __name__, url_prefix='/user', template_folder='../templates', static_folder='../static')

# 登录接口
@user.route('/login', methods=['GET','POST'])
def login():
    try:
        if request.method == 'GET':
            if session.get("islogin") == 1:
                return json_response(200, message="logined", data="[]")
            else:
                return json_response(500, message="not login", data="[]")
        if request.method == 'POST':
            username = request.form.get('user')
            password = hashlib.md5(request.form['pass'].encode(encoding='utf-8')).hexdigest()
            data = db.session.query(Users).filter(Users.username == username).filter(Users.password == password).first()
            if data:
                session.permanent = True
                session['islogin'] = 1
                session['username'] = username
                return json_response(200,message="login sucess")
            else:
                return json_response(500, message="username or password is wrong.")
    except Exception as e:
        logger.info("login api error,{}".format(e))


# 首页
@user.route('/index', methods=['GET'])
@check_login
def index():
    return "Home"


# 退出接口
@user.route('/logout', methods=['GET'])
def logout():
    session.permanent = True
    session["islogin"] = 0
    return json_response(200, message="logout sucess")

# 添加网站接口 添加后开始扫描
@user.route('/add_url', methods=['GET'])
def add_url():
	url = request.args['url']
	# 后台扫描js
	executor.submit(jsscan.scanjs, url)
	return 'ok{}'.format(url)

