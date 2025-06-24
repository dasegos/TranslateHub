from django.db import models
from django.core.exceptions import ValidationError

import re


def validate_menu_title(title: str):
    if re.findall(r'[А-Яа-яёЁ]', title):
        raise ValidationError('Menu titles cannot contain Cyrillic characters!')
    if re.findall(r'\s', title):
        raise ValidationError('Menu titles cannot contain spaces!')
    return title


class Menu(models.Model):
    '''`Menu` model.'''
    title = models.CharField(verbose_name='Menu title', max_length=30, blank=False, null=False, unique=True, validators=[validate_menu_title,])

    def __str__(self) -> str:
        return self.title


class MenuCategory(models.Model):
    '''`MenuCategory` model.'''
    menu   = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Menu', null=False, related_name='categories')
    title  = models.CharField(verbose_name='Menu title', max_length=30, blank=False, null=False, unique=True)
    url    = models.URLField(verbose_name='URL', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Parent category (if None, then it is parent category itself)', null=True, default=None)

    class Meta:
        verbose_name_plural = 'Menu categories'

    def __str__(self):
        return self.title