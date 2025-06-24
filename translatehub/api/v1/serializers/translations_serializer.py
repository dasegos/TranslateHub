from rest_framework import serializers

from translations.models import OriginalText, Translation, \
                                PostComment
from translations.config import LANGUAGES_USER_INTERFACE, WORK_TYPE_MODEL_CHOICE, \
                                PROFICIENCY_LEVELS_MODEL_CHOICE


class CommentSerializer(serializers.ModelSerializer):
    '''Comment serializer.'''

    content_object = serializers.SerializerMethodField(read_only=True)  

    def get_content_object(self, obj):
        return str(obj.content_object)

    class Meta:
        model = PostComment
        fields = ('pk',
                  'content_type',
                  'object_id',
                  'content_object',
                  'comment_text',
                  'posted_at',
                  'answer_to',
                  'author')


class OriginalTextsSerializer(serializers.ModelSerializer):
    '''Original texts serializer.'''
    language_name   = serializers.SerializerMethodField(read_only=True)  
    work_type = serializers.SerializerMethodField(read_only=True)  
    # proficiency_lvl = serializers.SerializerMethodField(read_only=True)  
    # suggested_lvl = serializers.SerializerMethodField(read_only=True) 
    likes_amount    = serializers.SerializerMethodField(read_only=True)  
    comments_amount = serializers.SerializerMethodField(read_only=True)
    comments        = CommentSerializer(many=True, read_only=True)

    def get_language_name(self, obj):
        return LANGUAGES_USER_INTERFACE[obj.language_code][0]
    
    def get_work_type(self, obj):
        return dict(WORK_TYPE_MODEL_CHOICE)[obj.work_type]
    
    def get_likes_amount(self, obj):
        return obj.likes.count()

    def get_comments_amount(self, obj):
        return obj.comments.count()

    class Meta:
        model = OriginalText
        fields = ('pk',
                  'title',
                  'slug',
                  'content',
                  'work_type',
                  'language_code',
                  'language_name',
                  'posted_at',
                  'last_upd',
                  'user',
                  'verified',
                  'proficiency_lvl',
                  'suggested_lvl',
                  'likes_amount',
                  'comments_amount',
                  'comments')


class TranslationSerializer(serializers.ModelSerializer):

    language_name   = serializers.SerializerMethodField(read_only=True)  
    work_type       = serializers.SerializerMethodField(read_only=True)  
    likes_amount    = serializers.SerializerMethodField(read_only=True)  
    comments_amount = serializers.SerializerMethodField(read_only=True)
    comments        = CommentSerializer(many=True, read_only=True)

    def get_language_name(self, obj):
        return LANGUAGES_USER_INTERFACE[obj.language_code][0]
    
    def get_work_type(self, obj):
        original_text = obj.original.pk
        original_text_work_type = OriginalText.objects.filter(pk=original_text).first().work_type
        return dict(WORK_TYPE_MODEL_CHOICE)[original_text_work_type]
    
    def get_likes_amount(self, obj):
        return obj.likes.count()

    def get_comments_amount(self, obj):
        return obj.comments.count()


    class Meta:
        model = OriginalText
        fields = ('pk',
                #   'original',
                  'title',
                  'slug',
                  'content',
                  'work_type',
                  'language_code',
                  'language_name',
                  'posted_at',
                  'last_upd',
                  'user',
                  'verified',
                  'proficiency_lvl',
                  'suggested_lvl',
                  'likes_amount',
                  'comments_amount',
                  'comments'
                  )
                #   'is_rhymed')
