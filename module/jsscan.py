#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 2:37 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : jsscan.py
# js 扫描模块 url参数


from libs.db_sql import *
from module.jsfinder import *

def scanjs(url):
    # 实现，通过第一遍扫描js 入库，然后定期扫描js，如果出现新的域名出现js，标记为告警
    # 更新状态 开始扫描
    add_site(url, 0)
    start_scan(url)
    return True

