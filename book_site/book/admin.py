from django.contrib import admin
from django.contrib.gis import forms
from django.utils.safestring import mark_safe

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BookAdminForm(forms.ModelForm):
    descriptions = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Book
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Category' """
    list_display = ('id', 'name', 'descriptions')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'descriptions')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Author' """
    list_display = ('id', 'name', 'get_image', 'country', 'age', 'biography')
    list_display_links = ('id', 'name', 'get_image')
    search_fields = ('name', 'country', 'biography')
    readonly_fields = ('get_image', )

    # Выводим изображение автора. Выводим стрку как html-тэг:
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.images.url} width="100" height="120">')

    get_image.short_description = 'Изображение'


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


class ReviewsInLineAdmin(admin.TabularInline):
    """ Админ-класс для отображения на админ-странице 'BookAdmin' список отзывов/комментариев """
    model = Reviews
    # Доп-поля:
    extra = 1
    # Блокировка на изменение:
    readonly_fields = ('name', 'email')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Reviews' """
    list_display = ('name', 'email', 'parent', 'book', 'id')
    readonly_fields = ('name', 'email')
    search_fields = ('name', 'book')


@admin.register(SuggestBook)
class SuggestBookAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'SuggestBook' """
    list_display = ('name', 'author', 'user_book', 'draft')
    readonly_field = ('name', 'author', )
    search_fields = ('name', 'author', )
    list_editable = ('draft', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """ Админ-класс для работы с 'Book' """
    # Список полей, которые будут доступны для настроек:
    list_display = ('id', 'name', 'year_edition', 'draft')
    # Список ссылочных полей:
    list_display_links = ('id', 'name')
    # Список полей, по которым можно будет производить поиск:
    search_fields = ('name', 'descriptions', 'category__name', 'genre__name')
    # Список полей для фильтрации
    list_filter = ('date_published', 'category__name', 'genre__name')
    # Отображение всех отзывов о книге:
    inlines = [ReviewsInLineAdmin]
    # Отображать меню сохранения сверху:
    save_on_top = True
    # Сохранить как новый объект:
    # save_as = True
    # Поля, которые мы можем сохранять не заходя в сам объект:
    list_editable = ('draft',)
    # Вывод постера на админ-панели:
    readonly_fields = ('get_image', )

    # Подключаем наши actions:
    actions = ["published", "unpublished"]

    # Form для ckeditor:
    form = BookAdminForm

    fieldsets = (
        ('Main', {
            'fields': (('name', 'year_edition', 'draft'), )
        }),
        (None, {
            'fields': ('descriptions', ('images', 'get_image'), )
        }),
        (None, {
            'fields': (('category', 'url'), )
        }),
        ('Base info', {
            'classes': ('collapse', ),
            'fields': (('genre', 'author', 'published_house', 'translation'), )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.images.url} width="200" height="260">')

    get_image.short_description = 'Постер'

    # Создаем actions:
    def unpublished(self, request, queryset):
        """ Снимаем книгу с положения 'опубликованно' (черновик): """

        row_update = queryset.update(draft=True)
        message_bit = f'Количество обновленных записей: {row_update}'

        self.message_user(request, f"{message_bit}")

    unpublished.short_description = "Снять с публикации"
    # Проверяет наличие у пользователя права на изменение:
    unpublished.allowed_permission = ("change", )

    def published(self, request, queryset):
        """ Ставим книгу в положение 'опубликованно' (черновик): """
        row_update = queryset.update(draft=False)
        message_bit = f'Количество обновленных записей: {row_update}'

        self.message_user(request, f'{message_bit}')

    published.short_description = "Опубликовать"
    published.allowed_permission = ("change", )


admin.site.site_title = 'MySiteBook'
admin.site.site_header = 'MySiteBook'
