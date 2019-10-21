#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Description: 日志API
@Author: Zpp
@Date: 2019-10-17 15:46:30
@LastEditors: Zpp
@LastEditTime: 2019-10-21 14:27:55
'''
from flask import Blueprint, request
from collection.log import LogModel
from ..token_auth import auth, validate_current_access
from libs.code import ResultDeal

route_log = Blueprint('Log', __name__, url_prefix='/v1/Log')


@route_log.route('/QueryLogByParam', methods=['POST'])
@auth.login_required
@validate_current_access
def QueryLogByParam():
    params = {}
    Int = ['type', 'status']
    for i in request.form:
        if i in Int:
            params[i] = int(request.form[i])
        else:
            params[i] = request.form[i]

    result = LogModel().QueryLogByParamRequest(
        params=params,
        page=int(request.form.get('page', 1)),
        page_size=int(request.form.get('page_size', 20))
    )

    if type(result).__name__ == 'str':
        return ResultDeal(msg=result, code=-1)

    return ResultDeal(data=result)
