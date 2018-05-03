from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse

from .models import Question, Category

class QuestionModelTests(TestCase):

    def test_question_str(self):
        future_question = Question(title = 'a')
        self.assertIs(future_question.__str__(), 'a')

    def test_question_str_2(self):
        future_question = Question(title = 'ab')
        self.assertIs(future_question.__str__(), 'ab')

    def test_question_str_3(self):
        future_question = Question(title = 'ac')
        self.assertIs(future_question.__str__(), 'ac')

class CategoryModelTests(TestCase):

    def test_category_str(self):
        cat = Category(text = 'txt')
        self.assertIs(cat.__str__(), 'txt')

    def test_category_str_2(self):
        cat = Category(text = 'Basic Info')
        self.assertIs(cat.__str__(), 'Basic Info')

    def test_category_str_3(self):
        cat = Category(text = 'Personal Info')
        self.assertIs(cat.__str__(), 'Personal Info')
