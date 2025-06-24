import re
from django import forms
from .models import OriginalText, Translation, TranslationRemark, PostComment


from .config import LANGUAGES_MODEL_CHOICE, PROFICIENCY_LEVELS_MODEL_CHOICE, \
                    WORK_TYPE_MODEL_CHOICE, IS_RHYMED_FORM_CHOICE


class OriginalTextForm(forms.ModelForm):
    class Meta:
        model = OriginalText
        fields = ['title', 'content', 'language_code', 'proficiency_lvl', 'work_type',]
        widgets = {
            'title'           : forms.TextInput(attrs={'class' : 'input_title', 'placeholder' : 'Введите заголовок'}),
            'content'         : forms.Textarea(attrs={'class' : 'input_area', 'placeholder' : 'Введите текст'}),
            'language_code'   : forms.ChoiceField(choices=LANGUAGES_MODEL_CHOICE),
            'proficiency_lvl' : forms.ChoiceField(choices=PROFICIENCY_LEVELS_MODEL_CHOICE),
            'work_type'       : forms.ChoiceField(choices=WORK_TYPE_MODEL_CHOICE),
        }


class TranslationForm(forms.ModelForm):
    class Meta:
        model = Translation
        fields = ['title', 'content', 'language_code', 'proficiency_lvl', 'is_rhymed',]
        widgets = {
            'title'           : forms.TextInput(attrs={'class' : 'input_title', 'placeholder' : 'Введите заголовок'}),
            'content'         : forms.Textarea(attrs={'class' : 'input_area', 'placeholder' : 'Введите текст'}),
            'language_code'   : forms.ChoiceField(choices=LANGUAGES_MODEL_CHOICE),
            'proficiency_lvl' : forms.ChoiceField(choices=PROFICIENCY_LEVELS_MODEL_CHOICE),
            'is_rhymed'       : forms.ChoiceField(choices=IS_RHYMED_FORM_CHOICE),
        }


class TranslationRemarkForm(forms.ModelForm):
    class Meta:
        model = TranslationRemark
        fields = ['remark_text',]
        widgets = { 
            'remark_text' : forms.Textarea(attrs={'class' : 'input_area', 'placeholder' : 'Введите текст'}),
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment_text',]
        widgets = {
            'comment_text' : forms.Textarea(attrs={'class' : 'input_area', 'placeholder' : 'Введите комментарий'}),
        }
