from django.contrib import admin

from .models import Book, Category, Author, PublishedHouse, Translation, Genre, Rating


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Category' """
    list_display = ('id', 'name', 'descriptions')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'descriptions')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Author' """
    list_display = ('id', 'name', 'country', 'age', 'biography')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'country', 'biography')


@admin.register(PublishedHouse)
class PublishedHouseAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'PublishedHouse' """
    list_display = ('id', 'name', 'country')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'country')


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Translation' """

    list_display = ('id', 'name_interpreter')
    list_display_links = ('id', 'name_interpreter')
    search_fields = ('name', 'name_interpreter')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Genre' """
    list_display = ('id', 'name', 'descriptions')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'descriptions')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Rating' """
    list_display = ('id', 'ip', 'book', 'stars')
    list_display_links = ('id', 'book')
    search_fields = ('book', )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Book' """
    # Список полей, которые будут доступны для настроек:
    list_display = ('id', 'name', 'descriptions', 'year_edition', 'draft')
    # Список ссылочных полей:
    list_display_links = ('id', 'name')
    # Список полей, по которым можно будет производить поиск:
    search_fields = ('name', 'descriptions')
    # Список полей для фильтрации
    list_filter = ('name', 'year_edition', 'date_published', 'category__name', 'author__name', 'genre__name')
