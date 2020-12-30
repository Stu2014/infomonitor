#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 4:48 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : main.py

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


# 转化数据
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