from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('api.v1.urls')),
    path('admin/', admin.site.urls),
    path('', include('translations.urls')),
    path('forum/', include('forum.urls')),
    # path('users/', include('users.urls')),
]
