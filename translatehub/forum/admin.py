from django.contrib import admin
from .models import Answer, Question, Category

@admin.register(Question)
class AdminOriginalText(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}

admin.site.register(Answer)

