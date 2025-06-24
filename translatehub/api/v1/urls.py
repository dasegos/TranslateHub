from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.user_view import UserViewSet
from .views.forum_view import QuestionViewSet, AnswerViewSet
from .views.translations_view import OriginalTextsViewSet, TranslationsViewSet, CommentsViewSet


v1_router = DefaultRouter()
v1_router.register('users', UserViewSet, basename='users')
v1_router.register('questions', QuestionViewSet, basename='questions')
v1_router.register('answers', AnswerViewSet, basename='answers')
v1_router.register('original-texts', OriginalTextsViewSet, basename='original-texts')
v1_router.register('translations', TranslationsViewSet, basename='translations')
v1_router.register('comments', CommentsViewSet, basename='comments')
# v1_router.register(r'courses/(?P<course_id>\d+)/lessons', LessonViewSet, basename='lessons')
# v1_router.register(r'courses/(?P<course_id>\d+)/groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('', include(v1_router.urls)),
    # path("auth/", include('djoser.urls')),
    # path("auth/", include('djoser.urls.authtoken')),
]