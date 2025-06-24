from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from translations.models import OriginalText, Translation, PostComment
from ..serializers.translations_serializer import OriginalTextsSerializer, TranslationSerializer,\
                                                  CommentSerializer


class OriginalTextsViewSet(viewsets.ModelViewSet):
    '''Original texts viewset.'''
    queryset = OriginalText.objects.all()
    serializer_class = OriginalTextsSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'patch', 'delete']
    # permission_classes = (permissions.IsAdminUser,)


class TranslationsViewSet(viewsets.ModelViewSet):
    '''Translations viewset.'''
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'patch', 'delete']
    # permission_classes = (permissions.IsAdminUser,)


class CommentsViewSet(viewsets.ModelViewSet):
    '''Comments viewset.'''
    queryset = PostComment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'delete']
    # permission_classes = (permissions.IsAdminUser,)