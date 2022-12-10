# Generated by Django 3.2.16 on 2022-12-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_suggestbook_user_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggestbook',
            name='draft',
            field=models.CharField(choices=[('1', 'Рассмотрена'), ('2', 'Рассматривается'), ('3', 'Отклонена')], default='Рассматривается', max_length=1, verbose_name='Стадия рассмотрения'),
        ),
        migrations.AlterField(
            model_name='suggestbook',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Описание книги'),
        ),
    ]
