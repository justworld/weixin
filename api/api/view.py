# -*- coding: utf- -*-

from django.http import JsonResponse
from .model import Account

#登陆
def login(request):
    return JsonResponse({'msg': 'hello,world'})

#注册
def reg(request):
    return JsonResponse({'msg': 'hello,world'})
