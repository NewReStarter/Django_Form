from django.db import models
from datetime import datetime
from django import forms
from django.utils.text import capfirst
from django.core import exceptions
from json import loads


# Create your models here.

class Category(models.Model):
    status = models.IntegerField(default=1)
    text = models.CharField(max_length=256)
    create_time = models.DateField(default=datetime.now)
    modify_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.text

    def to_object(self):
        return {
            'id': self.id,
            'status': self.status,
            'text': self.text,
            'create_time': self.create_time.strftime('%Y-%m-%d'),
            'modify_time': self.modify_time.strftime('%Y-%m-%d'),
        }


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    type = models.CharField(max_length=64)
    length = models.CharField(max_length=64, default='10')
    title = models.CharField(max_length=128)
    describe = models.CharField(max_length=1024)
    allow_multiple = models.BooleanField(default=True)
    require = models.BooleanField(default=True)
    create_time = models.DateField(default=datetime.now)
    modify_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.title

    def to_object(self):
        return {
            'id': self.id,
            'status': self.status,
            'type': self.type,
            'title': self.title,
            'describe': self.describe,
            'allow_multiple': self.allow_multiple,
            'require': self.require,
            'create_time': self.create_time.strftime('%Y-%m-%d'),
            'modify_time': self.modify_time.strftime('%Y-%m-%d'),
            'category_id': self.category_id,
            'length': self.length,
        }


class Option(models.Model):
    text = models.CharField(max_length=64)
    quetion = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Options'

    def __str__(self):
        return self.text


class Form_data(models.Model):
    data = models.CharField(max_length=16384)
    status = models.CharField(max_length=100, default='')
    create_time = models.DateField(default=datetime.now)
    modify_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Form_data"

    def __str__(self):
        return self.id

    def to_object(self):
        model = {
            'id': self.id,
            'status': self.status,
            'modify_time': self.modify_time.__str__(),
        }
        i = 0
        data = loads(self.data)
        for c in data:
            if i > 10:
                break
            for q in c['questions']:
                model['q%d' % i] = q['answer'][-1]
                i += 1
                if i > 10:
                    break
        return model
