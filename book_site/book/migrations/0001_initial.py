# Generated by Django 3.2.16 on 2022-11-24 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('date_birthday', models.DateField(default=None, verbose_name='Дата рождения:')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('images', models.ImageField(upload_to='book_site/', verbose_name='Постер')),
                ('biography', models.TextField(max_length=500, verbose_name='Биография')),
                ('url', models.SlugField(default='2', max_length=150)),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('images', models.ImageField(upload_to='book_site/', verbose_name='Постер')),
                ('descriptions', models.TextField(blank=True, verbose_name='Описание')),
                ('year_edition', models.PositiveSmallIntegerField(blank=True, verbose_name='Дата написания:')),
                ('date_published', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('url', models.SlugField(max_length=150)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('author', models.ManyToManyField(related_name='book_author', to='book.Author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-date_published'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('descriptions', models.TextField(max_length=500, verbose_name='Описание')),
                ('url', models.SlugField(default='1', max_length=150)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Жанр')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(default=1, max_length=150)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='PublishedHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Издатель',
                'verbose_name_plural': 'Издатели',
            },
        ),
        migrations.CreateModel(
            name='SuggestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('author', models.CharField(max_length=100, null=True, verbose_name='Автор книги')),
                ('text', models.TextField(max_length=5000, verbose_name='Впечатление о книге')),
                ('url_book', models.URLField(null=True, verbose_name='Ссылка на книгу')),
                ('draft', models.BooleanField(default=False, verbose_name='Стадия рассмотрения')),
            ],
            options={
                'verbose_name': 'Предложенная книга',
                'verbose_name_plural': 'Предложенные книги',
            },
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_interpreter', models.CharField(max_length=150, verbose_name='Автор перевода')),
                ('translate_date', models.DateField(default=None, verbose_name='Дата перевода')),
                ('translate_stage', models.CharField(max_length=50, verbose_name='Стадия перевода')),
            ],
            options={
                'verbose_name': 'Автор перевода',
                'verbose_name_plural': 'Авторы перевода',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book', verbose_name='Произведение')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.reviews', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='book.Genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='book',
            name='published_house',
            field=models.ManyToManyField(related_name='book_published_house', to='book.PublishedHouse', verbose_name='Издатель'),
        ),
        migrations.AddField(
            model_name='book',
            name='translation',
            field=models.ManyToManyField(related_name='book_translation', to='book.Translation', verbose_name='Перевод'),
        ),
    ]
