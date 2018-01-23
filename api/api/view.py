# -*- coding: utf- -*-

from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from .model import Account
from . import tool


# 登陆
@require_http_methods(['POST'])
def login(request):
    model = json.loads(request.body)
    if 'name' in model:
        username = model['name']
        password = model['password']
        if not username:
            return JsonResponse({'result': False, 'msg': '用户名为空'})
        if not password:
            return JsonResponse({'result': False, 'msg': '密码为空'})
        try:
            entity = Account.objects.get(name=username)
            if entity.password == tool.Md5Encrypt(password):
                return JsonResponse({'result': True})
            else:
                return JsonResponse({'result': False, 'msg': '密码错误'})
        except Account.DoesNotExist:
            return JsonResponse({'result': False, 'msg': '该用户名没有注册'})

    return JsonResponse({'result': False, 'msg': '未通过数据验证'})


# 注册
@require_http_methods(['POST'])
def reg(request):
    model = json.loads(request.body)
    if 'name' in model:
        username = model['name']
        password = model['password']
        if not username:
            return JsonResponse({'result': False, 'msg': '用户名为空'})
        if not password:
            return JsonResponse({'result': False, 'msg': '密码为空'})
        try:
            Account.objects.get(name=username)
            return JsonResponse({'result': False, 'msg': '该用户名已注册'})
        except Account.DoesNotExist:
            entity = Account(name=username, password=tool.Md5Encrypt(password))
            entity.save()
            return JsonResponse({'result': True})

    return JsonResponse({'result': False, 'msg': '未通过数据验证'})
