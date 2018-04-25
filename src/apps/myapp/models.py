from django.db import models
from datetime import datetime
from django import forms
from django.utils.text import capfirst
from django.core import exceptions


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


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    type = models.CharField(max_length=64)
    length = models.CharField(max_length=64)
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


class Option(models.Model):
    text = models.CharField(max_length=64)
    quetion = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Options'

    def __str__(self):
        return self.text


class Form_data(models.Model):
    data = models.CharField(max_length=16384)
    status = models.CharField(max_length=128)
    create_time = models.DateField(default=datetime.now)
    modify_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Form_data"

    def __str__(self):
        return self.id
