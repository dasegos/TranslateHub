from django.contrib import admin
from django.urls import path, include

from .views import CheckView


urlpatterns = [
    path('check/', CheckView.as_view()),
    path('<int:pk>/<slug:slug>/check', CheckView.as_view()),
]