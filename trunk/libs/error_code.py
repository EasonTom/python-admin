#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Description: 错误处理方法
@Author: Zpp
@Date: 2019-09-04 17:09:14
@LastEditTime: 2019-10-15 13:46:40
@LastEditors: Zpp
'''
from flask import jsonify
from models.log import Log
from models.base import db
import logging


def ResultDeal(code=0, data={}, msg=''):
    return jsonify({
        'code': code,
        'data': data,
        'msg': msg
    })


def RecordLog(src, error):
    logging.error(error)
    s = db.session()
    item = Log(
        src=src,
        content=error.message
    )
    s.add(item)
    s.commit()
    s.close()
    return str(error.message)
