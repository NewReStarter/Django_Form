from django.shortcuts import render
from django.views.generic.base import View
from .models import *
import json


class FormView(View):
    def get(self, request):
        categories = Category.objects.filter(status=1)
        return render(request, "index.html", {'categories': categories})

    def post(self, request):
        data = []
        check_list = {}
        q_check_list = {}
        for k, v in request.POST.items():
            category = Category.objects.get(id=k.split('_')[0])
            question = Question.objects.get(id=k.split('_')[1])
            if check_list.__contains__(category.id):
                if len(k.split('_')) == 3:
                    c_index = check_list[category.id]['count']
                    q_index = check_list[category.id]['question'][question.id]
                    data[c_index]['questions'][q_index]['answer'].append(v)
                else:
                    data[check_list[category.id]['count']]['questions'].append({
                        'answer': [v],
                        'id': question.id,
                        'text': question.title,
                        'addtion_info': question.describe,
                    })
                    check_list[category.id]['question'][question.id] = len(check_list[category.id]['question'])
            else:
                data.append({
                    'id': category.id,
                    'text': category.text,
                    'questions': [{
                        'answer': [v],
                        'id': question.id,
                        'text': question.title,
                        'addtion_info': question.describe,
                    }],
                })
                check_list[category.id] = {
                    'count': len(data) - 1,
                    'question': {
                        question.id: 0
                    }
                }
        form_data = Form_data()
        form_data.data = json.dumps(data)
        form_data.create_time = datetime.now()
        form_data.modify_time = datetime.now()
        form_data.save()
        categories = Category.objects.filter(status=1)
        return render(request, "index.html", {'categories': categories})
