from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


user = get_user_model()


class QuestionManager(models.Manager):
    
    def newest(self) -> models.QuerySet:
        queryset = super().get_queryset().order_by('-pk').all()
        return queryset

    def no_answers(self) -> models.QuerySet:
        ...

    def no_accepted_answers(self) -> models.QuerySet:
        ...

    def most_liked(self) -> models.QuerySet:
        queryset = super().get_queryset().order_by('-likes').all()
        return queryset
    
    def has_categories(self, categories: dict) -> models.QuerySet:
        ...


class Question(models.Model):
    title       = models.CharField(verbose_name='Title', max_length=100, blank=False, null=False)
    text        = models.TextField(verbose_name='Description', blank=False, null=False)
    slug        = models.SlugField(verbose_name='Slug', max_length=100, unique=True)
    created_at  = models.DateTimeField(verbose_name='Creation datetime', auto_now_add=True)
    author      = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='Author', related_name='questions')
    categories  = models.ManyToManyField('Category', related_name='questions', verbose_name='Question categories')
    likes       = GenericRelation('StateLike')

    questions   = QuestionManager()
    objects     = models.Manager()


class Answer(models.Model):
    text        = models.TextField(verbose_name='Answer', blank=False, null=False)
    question    = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Question', related_name='answers')
    answered_at = models.DateTimeField(verbose_name='Answer datetime', auto_now_add=True)
    is_accepted = models.BooleanField(verbose_name='Is accepted', default=False, blank=True, null=False, editable=False)
    author      = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='Author', related_name='answers')
    likes       = GenericRelation('StateLike')


class Category(models.Model):
    title = models.CharField(verbose_name='Category title', max_length=30, blank=False, null=False, unique=True)
    slug  = models.SlugField(verbose_name='Slug', max_length=30, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title

class StateLike(models.Model):
    content_type   = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Model instance reference', limit_choices_to=Q(app_label='forum', model='question') | Q(app_label='forum', model='answer'))
    object_id      = models.PositiveIntegerField(verbose_name='Real instance ID')
    content_object = GenericForeignKey('content_type', 'object_id')
    author         = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='User instance')


