from .models import *
import xadmin


class OptionInline(object):
    model = Option
    extra = 3
    style = 'accordion'


class QuestionInline(object):
    model = Question
    extra = 3
    style = 'accordion'


class CategoryAdmin(object):
    list_display = ['id', 'status', 'text', 'create_time', 'modify_time']
    search_fields = ['id', 'status', 'text', ]
    list_filter = ['id', 'status', 'text', 'create_time', 'modify_time']
    show_detail_fields = ['text']
    list_per_page = 20
    list_export = ('xls', 'xml', 'json', 'csv')
    list_export_fields = ('id', 'status', 'text', 'create_time', 'modify_time')
    inlines = [QuestionInline]


class QuestionAdmin(object):
    list_display = ['id', 'status', 'type', 'title', 'describe', 'require', 'allow_multiple', 'create_time',
                    'modify_time']
    search_fields = ['id', 'status', 'title', 'describe']
    list_filter = ['id', 'status', 'type', 'title', 'describe', 'require', 'allow_multiple', 'create_time',
                   'modify_time']

    list_export = ('xls', 'xml', 'json', 'csv')
    list_export_fields = ('id', 'status', 'type', 'title', 'describe', 'require', 'allow_multiple', 'create_time',
                          'modify_time')
    inlines = [OptionInline]


class Form_DataAdmin(object):
    list_display = ['id', 'data', 'create_time', 'modify_time']
    search_fields = ['data']
    list_filter = ['id', 'data', 'create_time', 'modify_time']


class OptionAdmin(object):
    list_display = ['id', 'text']
    search_fields = ['text']
    list_filter = ['text']


class GlobalSetting(object):
    menu_style = 'default'  # 'accordion'


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Option, OptionAdmin)
xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(Form_data, Form_DataAdmin)
