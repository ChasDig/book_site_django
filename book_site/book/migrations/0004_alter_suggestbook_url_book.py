# Generated by Django 3.2.16 on 2022-12-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_suggestbook_url_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestbook',
            name='url_book',
            field=models.URLField(default='', null=True, verbose_name='Ссылка на книгу'),
        ),
    ]