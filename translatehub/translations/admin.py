from django.contrib import admin

from .menu_models import Menu, MenuCategory
from .models import OriginalText, Translation, TranslationRemark, PostComment, PostLike


@admin.register(OriginalText)
class AdminOriginalText(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}

@admin.register(Translation)
class AdminTranslation(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title', )}

admin.site.register(TranslationRemark)
admin.site.register(PostComment)
admin.site.register(PostLike)
admin.site.register(Menu)
admin.site.register(MenuCategory)