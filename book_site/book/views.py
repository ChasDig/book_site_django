from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .models import *
from .forms import *


class CategoryGenre:
    """ Класс для получение моделей Категорий и Жанров """

    def get_category(self):
        return Category.objects.all()

    def get_genre(self):
        return Genre.objects.all()


class BookViews(CategoryGenre, ListView):
    """ Класс-контроллер для работы с главной страниц 'book_all_list' """

    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book'
    queryset = Book.objects.filter(draft=False)

    paginate_by = 2

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


class BookOneDataViews(CategoryGenre, DetailView):
    """ Контроллер-класс для работы со страницей книги """

    model = Book

    template_name = 'book/book_detail.html'
    context_object_name = 'book_data'

    slug_field = 'url'


class CategoryViews(CategoryGenre, DetailView):

    model = Category
    template_name = 'book/category_detail.html'
    context_object_name = 'category'

    slug_field = 'url'

    paginate_by = 2

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


class FilterBookViews(CategoryGenre, ListView):
    """ Контроллер-класс для работы с категориями"""

    context_object_name = 'book'

    paginate_by = 2

    def get_queryset(self):
        queryset = Book.objects.filter(Q(category__in=self.request.GET.getlist("categories")) |
                                       Q(genre__in=self.request.GET.getlist("genre")))
        print(queryset)
        return queryset


class AuthorDataViews(DetailView):
    """ Контроллер-класс для работы с авторами """
    model = Author

    template_name = 'book/author_detail.html'
    context_object_name = 'author_one'
    slug_field = 'url'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['book_categories'] = Category.objects.all()
        context['genre'] = Genre.objects.all()
        context['books'] = Book.objects.all()
        print(context)

        return context


class ReviewsViews(View):
    """ Контроллер-класс для добавления комментария к произведению """

    def post(self, request, pk):

        form = ReviewsForm(request.POST)
        book = Book.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.book_id = pk
            form.save()

        return redirect(book.get_absolute_url())


class SearchBook(ListView):
    """ Контроллер-функция для поиска книг по названию """

    # Поиск по названию без учета регистра:
    def get_queryset(self):
        return Book.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        print(context)

        return context
