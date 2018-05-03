from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize


# Register your models.py here.
def action_login_auth(func):
    def in_fun(request):
        if request.session.get("userid"):
            return func(request)
        else:
            return HttpResponseRedirect('/myadmin/home/login')

    return in_fun


def api_login_auth(func):
    def in_fun(request):
        if request.session.get("userid"):
            return func(request)
        else:
            return HttpResponse(serialize({
                'code': 600,
                'msg': '登录过期'
            }))

    return in_fun


def post_action(func):
    def in_fun(request):
        if request.method == 'POST':
            return func(request)
        else:
            return HttpResponse(serialize({
                'code': 404,
                'msg': '只能使用post方式访问'
            }))

    return in_fun


def get_action(func):
    def in_fun(request):
        if request.method == 'GET':
            return func(request)
        else:
            return HttpResponse(serialize({
                'code': 404,
                'msg': '只能使用get方式访问'
            }))

    return in_fun
