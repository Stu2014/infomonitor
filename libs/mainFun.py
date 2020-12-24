#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 4:48 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : mainFun.py

import functools
from flask import make_response, jsonify, redirect, url_for, request, session

# 通用返回
def json_response(code=502, data=[], message="sucess"):
    resp = make_response(jsonify({"code": code, "data": data, "message": message}))
    resp.headers["Content-Type"] = "application/json"
    return resp

# 检查登录
def check_login(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        session_ = session.get('islogin')

        if session_ == 1:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user.login'))
    return inner