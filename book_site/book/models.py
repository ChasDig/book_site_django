from django.db import models


class Category(models.Model):
    """Модель: Категории"""

    name = models.CharField(verbose_name='Категория', max_length=150)
    descriptions = models.TextField(verbose_name='Описание', max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(models.Model):
    """Модель: Автор"""
    name = models.CharField(verbose_name='Имя', max_length=150)
    date_birthday = models.DateField(verbose_name='Дата рождения:', default=None)
    country = models.CharField(verbose_name='Страна', max_length=50)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    images = models.ImageField(verbose_name='Постер', upload_to='book_site/')
    biography = models.TextField(verbose_name='Биография', max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class PublishedHouse(models.Model):
    """Модель: Издатель"""
    name = models.CharField(verbose_name='Имя', max_length=150)
    country = models.CharField(verbose_name='Страна', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Translation(models.Model):
    """Модель: Автор перевода"""
    name_interpreter = models.CharField(verbose_name='Автор перевода', max_length=150)
    translate_date = models.DateField(verbose_name='Дата перевода', default=None)
    translate_stage = models.CharField(verbose_name='Стадия перевода', max_length=50)

    def __str__(self):
        return self.name_interpreter

    class Meta:
        verbose_name = 'Автор перевода'
        verbose_name_plural = 'Авторы перевода'


class Genre(models.Model):
    """Модель: Жанр"""
    name = models.CharField(verbose_name='Имя', max_length=150)
    descriptions = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    """Модель: Книг"""

    name = models.CharField(verbose_name='Название', max_length=150)
    images = models.ImageField(verbose_name='Постер', upload_to='book_site/')
    descriptions = models.TextField(verbose_name='Описание')
    year_edition = models.PositiveSmallIntegerField(verbose_name='Дата написания:', default=2000)
    date_published = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    url = models.SlugField(max_length=150)
    draft = models.BooleanField(verbose_name='Черновик', default=False)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    author = models.ManyToManyField(Author, verbose_name='Автор', related_name='book_author')
    published_house = models.ManyToManyField(PublishedHouse, verbose_name='Издатель',
                                             related_name='book_published_house')
    translation = models.ManyToManyField(Translation, verbose_name='Перевод', related_name='book_translation')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-date_published']


class Stars(models.Model):
    """Модель: Звезды рейтинга"""

    values = models.PositiveSmallIntegerField(verbose_name='Значение', default=0)

    def __str__(self):
        return self.values

    class Meta:
        verbose_name = 'Звезда рейинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    """Модель: Рейтинг"""

    ip = models.CharField(verbose_name='IP-адрес', max_length=15)

    book = models.ForeignKey(Book, verbose_name='Книга', on_delete=models.CASCADE)
    stars = models.ForeignKey(Stars, verbose_name='Звезда', on_delete=models.CASCADE)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
