#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/22 4:05 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : portscan.py

import socket
ip ="127.0.0.1"
for x in range(1,82):
    try:
        s = socket.socket()
        s.connect((ip, x))
        print("{} is open ".format(x))
    except Exception as e:
        # print(e)
        pass
