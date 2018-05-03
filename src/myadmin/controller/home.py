from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from json import dumps
from myadmin.admin import *
from django.contrib.auth import authenticate


# 主页
@get_action
@action_login_auth
def index(request):
    return render(request, 'myindex.html', {
        'userName': request.session['userName']
    })


# 登录
@get_action
def login(request):
    return render(request, 'login.html')


# 登出
@get_action
@action_login_auth
def loginOut(request):
    del request.session['userid']
    del request.session['userName']
    return HttpResponseRedirect('/myadmin/home/login')


# 接口


# 登录
@post_action
def loginIn(request):
    try:
        data = {
            'code': 200,
            'msg': ''
        }
        user = authenticate(username=request.POST.get('name'), password=request.POST.get('password'))
        request.session['userid'] = user.id
        request.session['userName'] = user.username
        return HttpResponse(dumps(data))
    except Exception as ex:
        return HttpResponse(dumps({
            'code': 500,
            'msg': '用户名或密码错误'
        }))
