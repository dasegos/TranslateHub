from django.contrib import admin
from django.urls import path, include

from .views import questions, tags, QuestionView, AskView


urlpatterns = [
    path('questions/', questions, name='questions'),
    path('questions/tags', tags, name='tags'),
    path('questions/<int:pk>/<slug:slug>', QuestionView.as_view(), name='question'),
    path('questions/ask', AskView.as_view(), name='ask'),
]