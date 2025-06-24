from django.contrib import admin
from django.urls import path, include

from .views import main, about, original_texts, translations, \
                   OriginalTextView,  TranslationView, TranslateView


urlpatterns = [
    path('main/', main, name='main'),
    path('about/', about, name='about'),
    path('original-texts/', original_texts, name='original_texts'),
    path('original-texts/<int:pk>/<slug:slug>', OriginalTextView.as_view(), name='original_text'),
    path('translations/', translations, name='translations'),
    path('translations/<int:pk>/<slug:slug>', TranslationView.as_view(), name='translation'),
    path('original-texts/<int:pk>/<slug:slug>/translate', TranslateView.as_view(), name='translate'),
]