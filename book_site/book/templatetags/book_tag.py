from django import template

from ..models import *

# Регестрируем templatetags:
register = template.Library()


@register.simple_tag()
def get_categories():
    """ Получаем список всех категорий: """
    return Category.objects.all()


@register.simple_tag()
def get_genre():
    """ Получаем список всех жанров: """
    return Genre.objects.all()


@register.inclusion_tag('book/tags/last_book.html')
def get_last_book():
    last_book = Book.objects.order_by("-id")[:2]
    return {'last_book': last_book}
