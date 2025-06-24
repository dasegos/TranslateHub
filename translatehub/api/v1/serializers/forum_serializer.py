from django.contrib.auth import get_user_model
from rest_framework import serializers

from forum.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('pk',
                  'title',
                  'text',
                  'slug',
                  'created_at',
                  'author'
                  )



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk',
                  'text',
                  'question',
                  'answered_at',
                  'author'
                  )
