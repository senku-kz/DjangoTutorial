from django import template
from app01.models import *

register = template.Library()


@register.simple_tag(name='get_cats')
def get_categories(filter=None):
    """
    Это "simple_tag" - "Простой тэг"
    Возвращает коллекцию данных которая далее используется в шаблоне
    :return:
    """
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('app01/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    """
    Это "inclusion_tag" - "Включающий тэг"
    он возвращает фрагмент HTML страницы
    :return:
    """
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}
