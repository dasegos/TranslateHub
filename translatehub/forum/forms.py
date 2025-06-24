import re
from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text',]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'input_title', 'placeholder' : 'Введите вопрос (кратко, но емко)'}),
            'text'  : forms.Textarea(attrs={'class' : 'input_area', 'placeholder' : 'Введите описание вопроса'})
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text',]
        widgets = {
            'text' : forms.Textarea(attrs={'class' : 'input_area', 'placeholder' : 'Введите текст'})
        }


class SearchQuestionForm(forms.Form):
    pattern = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class' : 'input_text',
                                                            'placeholder' : 'Поиск' }))