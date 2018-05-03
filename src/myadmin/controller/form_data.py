from django.shortcuts import render
from django.http import HttpResponse
from myadmin.admin import *
from django.db.models import Q
from django.core.paginator import Paginator
from json import dumps, loads
from myapp.models import Form_data
from pdfkit import pdfkit
import reportlab
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from myapp.utils import extract_request_variables
import os


@get_action
@action_login_auth
def list(request):
    data = {
        '10-20': {
            'age': 0,
            'english': 0,
            'chinese': 0,
            'french': 0,
            'female': 0,
            'male': 0
        },
        '20-30': {
            'age': 0,
            'english': 0,
            'chinese': 0,
            'french': 0,
            'female': 0,
            'male': 0
        },
        '30-40': {
            'age': 0,
            'english': 0,
            'chinese': 0,
            'french': 0,
            'female': 0,
            'male': 0
        },
        '40-50': {
            'age': 0,
            'english': 0,
            'chinese': 0,
            'french': 0,
            'female': 0,
            'male': 0
        },
        '50-60': {
            'age': 0,
            'english': 0,
            'chinese': 0,
            'french': 0,
            'female': 0,
            'male': 0
        },
        '60 or above': {
            'age': 0,
            'english': 0,
            'chinese': 0,
            'french': 0,
            'female': 0,
            'male': 0
        },
        'all': 0
    }
    for item in Form_data.objects.filter(data__contains='{"id": 4').all():
        form_data = loads(item.data)
        for c in form_data:
            if c['id'] is 4:
                data[c['questions'][0]['answer'][0]]['age'] += 1
                data[c['questions'][0]['answer'][0]][c['questions'][1]['answer'][0]] += 1
                data[c['questions'][0]['answer'][0]][c['questions'][2]['answer'][0]] += 1
                data['all'] += 1
    return render(request, 'form_data/list.html', {
        'token': request.COOKIES.get("csrftoken"),
        'data': data
    })


@get_action
@action_login_auth
def detail(request):
    return render(request, 'form_data/detail.html', {
        'token': request.COOKIES.get("csrftoken"),
        'data': loads(Form_data.objects.filter(id=request.GET.get('id')).first().data),
        'result': True,
        'id': request.GET.get('id')
    })


# Create your views here.


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL  # Typically /static/
    sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL  # Typically /static/media/
    # Typically /home/userX/project_static/media/
    mRoot = settings.MEDIA_ROOT

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def download(request):
    template_path = 'form_data/detail.html'
    # context = extract_request_variables(request)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    template = get_template(template_path)
    html = template.render({
        'data': loads(Form_data.objects.filter(id=request.GET.get('id')).first().data),
        'result': False
    })
    if request.POST.get('show_html', ''):
        response['Content-Type'] = 'application/text'
        response['Content-Disposition'] = 'attachment; filename="report.txt"'
        response.write(html)
    else:
        pisaStatus = pisa.CreatePDF(
            html, dest=response, link_callback=link_callback)
        if pisaStatus.err:
            return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisaStatus.err,
                                                                                   html))
        return response


@post_action
@api_login_auth
def GetList(request):
    order = request.POST.get('order')
    sort = request.POST.get('sort')
    offset = int(request.POST.get('offset') if request.POST.get('offset') else 0)
    limit = int(request.POST.get('limit') if request.POST.get('offset') else 5)
    list = Form_data.objects.order_by(sort if order is 'ase' else '-' + sort).all()
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
def ChangeStatus(request):
    form_data = Form_data.objects.get(id=request.POST.get('id', 0))
    form_data.status = request.POST.get('status', '')
    form_data.save()
    return HttpResponse(200)
