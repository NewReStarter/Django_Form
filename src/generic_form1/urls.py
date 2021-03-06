"""generic_form1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic.base import RedirectView
from django.urls import path, re_path
import xadmin
from myadmin import views as myadmin_views

from myapp.views import *

urlpatterns = [
    path('myadmin/', myadmin_views.target),
    path('myadmin/<str:controller_name>/<str:action_name>', myadmin_views.target),
    path('xadmin/', xadmin.site.urls),
    # re_path('^admin-pdf/$', PDFView.as_view()),
    re_path('^$', FormView.as_view(), name="Form"),
    re_path('^form_data$', FormView.as_view(), name="form_data"),
    re_path('^favicon.ico$', RedirectView.as_view(url=r'static/favicon.ico')),
]
