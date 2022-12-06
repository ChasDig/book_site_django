from django.db.models import Q
from django.views.generic import *
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout


from .forms import *


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('book_views')
        else:
            messages.error(request, 'Ошибка при регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'book/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('book_views')
    else:
        form = UserLoginForm()
    return render(request, 'book/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class BookViews(ListView):
    """ Класс-контроллер для работы с главной страниц 'book_list' """

    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book'
    queryset = Book.objects.filter(draft=False)

    paginate_by = 2

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


class BookOneDataViews(DetailView):
    """ Контроллер-класс для работы со страницей книги """

    model = Book

    template_name = 'book/book_detail.html'
    context_object_name = 'book_data'

    slug_field = 'url'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['form'] = ReviewsForm()

        return context


class CategoryViews(DetailView):

    model = Category
    template_name = 'book/category_detail.html'
    context_object_name = 'category'

    slug_field = 'url'

    paginate_by = 2

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        return context


class FilterBookViews(ListView):
    """ Контроллер-класс для фильтрации книг"""

    context_object_name = 'book'

    paginate_by = 2

    def get_queryset(self):
        queryset = Book.objects.filter(Q(category__in=self.request.GET.getlist("categories")) |
                                       Q(genre__in=self.request.GET.getlist("genre"))).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context['categories'] = ''.join([f'categories={buf}&' for buf in self.request.GET.getlist("categories")])
        context['genre'] = ''.join([f'genre={buf}&' for buf in self.request.GET.getlist("genre")])
        return context


class AuthorDataViews(DetailView):
    """ Контроллер-класс для работы с авторами """
    model = Author

    template_name = 'book/author_detail.html'
    context_object_name = 'author_one'
    slug_field = 'url'


class SearchBook(ListView):
    """ Контроллер-функция для поиска книг по названию """

    paginate_by = 2
    context_object_name = 'book'

    def get_queryset(self):
        return Book.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context['q'] = f"q={self.request.GET.get('q')}&"
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


class SuggestBookViews(View):

    template_name = 'book/suggest_book.html'
    context_object_name = 'suggest_book'

    def get(self, request):

        form = SuggestBookForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = SuggestBookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо за предложенную книгу. Мы ее обязательно рассмотрим!')
            return redirect('book_views')
        else:
            messages.success(request, 'Вы ввели что-то не так. Повторите пожалуйста попытку!')
            return render(request, 'book/suggest_book.html', {'form': form})
