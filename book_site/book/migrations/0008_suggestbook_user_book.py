# Generated by Django 3.2.16 on 2022-12-01 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20221201_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestbook',
            name='user_book',
            field=models.FileField(blank=True, upload_to='user_book/1', verbose_name='Книга пользователя'),
        ),
    ]