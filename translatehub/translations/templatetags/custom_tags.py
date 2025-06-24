from django import template


from translations.menu_models import Menu, MenuCategory



register = template.Library()




@register.inclusion_tag('translations/tags/main_menu.html', name='menu_tag', takes_context=True)
def draw_menu(context, menu_title: str):
    categories = MenuCategory.objects.filter(menu__title=menu_title)
    values = categories.values()
    super_parents = [item for item in values.filter(parent=None)]
    