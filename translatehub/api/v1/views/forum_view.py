from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from forum.models import Question, Answer
from ..serializers.forum_serializer import QuestionSerializer, AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    '''Questions texts viewset.'''
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'delete']
    # permission_classes = (permissions.IsAdminUser,)


class AnswerViewSet(viewsets.ModelViewSet):
    """Questions texts viewset."""
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'delete']
    # permission_classes = (permissions.IsAdminUser,)
