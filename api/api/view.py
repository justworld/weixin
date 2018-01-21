# -*- coding: utf- -*-

from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from .model import Account


# 登陆
def login(request):
    return JsonResponse({'msg': 'hello,world'})


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
        exist = Account.objects.get(name=username)
        if exist:
            return JsonResponse({'result': False, 'msg': '该用户名已注册'})

        entity = Account(username, password)
        entity.save()
        return JsonResponse({'result': True, 'msg': '注册成功'})

    return JsonResponse({'result': False, 'msg': '未通过数据验证'})
