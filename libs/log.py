#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/23 3:15 下午
# @Author  : Pickmea.
# @Email   : h4ckst5@qq.com
# @File    : log.py

from loguru import logger
import datetime,os,pathlib

rq = datetime.datetime.now().year
# print(os.path.dirname(os.path.abspath(__file__)))

log_path = str(pathlib.Path(__file__).parent)+'/../log/'
log_name = log_path + str(rq)+'.log'
logger.add(log_name, format="{time} {level} {message}", rotation='5 MB', level="INFO")
