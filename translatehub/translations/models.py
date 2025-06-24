from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from .config import LANGUAGES_MODEL_CHOICE, WORK_TYPE_MODEL_CHOICE, \
                    PROFICIENCY_LEVELS_MODEL_CHOICE


user = get_user_model()


class Post(models.Model):
    '''`Post` model. Used as a parent abstract model for models `OriginalText` and `Translation`.'''
    title           = models.CharField(verbose_name='Title', max_length=100, blank=False, null=False)
    slug            = models.SlugField(verbose_name='Slug', max_length=150, unique=True, null=False)
    content         = models.TextField(verbose_name='Content', blank=False, null=False)
    language_code   = models.IntegerField(verbose_name='Language ID', choices=LANGUAGES_MODEL_CHOICE, blank=False, null=False)
    posted_at       = models.DateTimeField(verbose_name='Posted at', auto_now_add=True, editable=False)
    last_upd        = models.DateTimeField(verbose_name='Last updated', auto_now=True, editable=False)
    user            = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='User instance', related_name='%(class)s_related')
    verified        = models.BooleanField(verbose_name='Is verified', blank=False, null=False, default=False)
    proficiency_lvl = models.IntegerField(verbose_name='Proficiency level ID', choices=PROFICIENCY_LEVELS_MODEL_CHOICE, blank=False, null=False)
    suggested_lvl   = models.IntegerField(verbose_name='AI-suggested proficiency level ID', choices=PROFICIENCY_LEVELS_MODEL_CHOICE, null=True, default=None)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title


class OriginalText(Post):
    '''`OriginalText` model.'''
    work_type = models.IntegerField(verbose_name='Work type (prose/poetry)', choices=WORK_TYPE_MODEL_CHOICE, blank=False, null=False)
    comments  = GenericRelation('PostComment')
    likes     = GenericRelation('PostLike')


class Translation(Post):
    '''`Translation` model.'''
    original  = models.ForeignKey(OriginalText, on_delete=models.CASCADE, verbose_name='Original text instance')
    is_rhymed = models.BooleanField(verbose_name='Poetic translation (for poems only)', null=True, default=None)
    comments  = GenericRelation('PostComment')
    likes     = GenericRelation('PostLike')


class TranslationRemark(models.Model):
    '''`TranslationRemark` model.'''
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE, verbose_name='Translation instance')
    remark_text = models.CharField(verbose_name='Remark content', max_length=250, blank=False, null=False)
    digit_start = models.IntegerField(verbose_name='Start digit', blank=False, null=False)
    digit_end   = models.IntegerField(verbose_name='End digit', blank=False, null=False)


class PostComment(models.Model):
    '''`PostComment` model.'''
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Model instance reference', related_name='comments', limit_choices_to=Q(app_label='translations', model='originaltext') | Q(app_label='translations', model='translation'))
    object_id      = models.PositiveIntegerField(verbose_name='Real instance ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    comment_text   = models.TextField(verbose_name='Comment content', blank=False, null=False)
    posted_at      = models.DateTimeField(verbose_name='Posted at', auto_now_add=True, editable=False)
    answer_to      = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Answer to comment instance', blank=True, null=True)
    author         = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='User instance')


class PostLike(models.Model):
    '''`PostLike` model.'''
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Model instance reference', related_name='likes')
    object_id      = models.PositiveIntegerField(verbose_name='Real instance ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    author         = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='User instance')


class Category(models.Model):
    '''`Category` model.'''
    title   = models.CharField(verbose_name='Title', max_length=30, blank=False, null=False, unique=True)
    slug    = models.SlugField(verbose_name='Slug', max_length=40, unique=True, null=False)


class Band(models.Model):
    '''`Band` model.'''
    name = models.CharField(verbose_name='Title', max_length=100, blank=False, null=False, unique=True)
    slug = models.SlugField(verbose_name='Slug', max_length=100, unique=True, null=False)
    desc = models.CharField(verbose_name='Description', max_length=300, blank=False, null=False)


class Author(models.Model):
    '''`Author` model.'''
    full_name = models.CharField(verbose_name='Title', max_length=100, blank=False, null=False)
    slug      = models.SlugField(verbose_name='Slug', max_length=100, unique=True, null=False)
    desc      = models.CharField(verbose_name='Description', max_length=300, blank=False, null=False)