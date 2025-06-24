from django.views import View
from django.shortcuts import render

from .forms import SearchQuestionForm
from .models import Question, Answer, Category


def questions(request):
    question_categories = Category.objects.all()
    questions = Question.objects.all()
    return render(request, 'forum/questions.html', 
                  context={'search_question_form' : SearchQuestionForm,
                           'question_categories'  : question_categories,
                           'questions_list'       : questions,
                           })


def tags(request):
    return render(request, 'forum/tags.html', {})


class QuestionView(View):

    def get(self, request):
        ...

    def post(self, request):
        ...


class AskView(View):    
    def get(self, request):
        ...

    def post(self, request):
        ...
