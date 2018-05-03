from django.shortcuts import render
from django.http import HttpResponse
from myadmin.admin import *
from django.db.models import Q
from django.core.paginator import Paginator
from json import dumps
from myapp.models import Question


@get_action
@action_login_auth
def list(request):
    return render(request, 'question/list.html', {
        'token': request.COOKIES.get("csrftoken"),
        'id': request.GET.get('id')
    })


@post_action
@api_login_auth
def GetList(request):
    where = Q(category_id=request.POST.get('id'))
    title = request.POST.get('search')
    if title:
        where = Q(title__contains=title)
    order = request.POST.get('order')
    sort = request.POST.get('sort')
    offset = int(request.POST.get('offset') if request.POST.get('offset') else 0)
    limit = int(request.POST.get('limit') if request.POST.get('offset') else 5)
    list = Question.objects.filter(where).order_by(sort if order is 'ase' else '-' + sort).all()
    p = Paginator(list, limit)
    rows = []
    for item in p.page(offset // limit + 1).object_list:
        rows.append(item.to_object())
    return HttpResponse(dumps({
        'total': p.count,
        'rows': rows
    }))
