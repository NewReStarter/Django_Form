from django.shortcuts import render
from django.http import HttpResponse
from myadmin.admin import *
from django.db.models import Q
from django.core.paginator import Paginator
from json import dumps
from myapp.models import Category


@get_action
@action_login_auth
def list(request):
    return render(request, 'category/list.html', {
        'token': request.COOKIES.get("csrftoken")
    })


@post_action
@api_login_auth
def GetList(request):
    where = Q()
    text = request.POST.get('search')
    if text:
        where = Q(text__contains=text)
    order = request.POST.get('order')
    sort = request.POST.get('sort')
    offset = int(request.POST.get('offset') if request.POST.get('offset') else 0)
    limit = int(request.POST.get('limit') if request.POST.get('offset') else 5)
    list = Category.objects.filter(where).order_by(sort if order is 'ase' else '-' + sort).all()
    p = Paginator(list, limit)
    rows = []
    for item in p.page(offset // limit + 1).object_list:
        rows.append(item.to_object())
    return HttpResponse(dumps({
        'total': p.count,
        'rows': rows
    }))


@post_action
@api_login_auth
def Delete(request):
    id = request.POST.get('id')
    if (id):
        team = Category.objects.get(id=id)
        team.delete()
    return HttpResponse(200)
