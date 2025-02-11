# Generated by Django 2.2.2 on 2019-07-01 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20190701_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body_en',
            field=models.TextField(blank=True, db_index=True, verbose_name='Body:'),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_hy',
            field=models.TextField(blank=True, db_index=True, verbose_name='Մարմին:'),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_ru',
            field=models.TextField(blank=True, db_index=True, verbose_name='Тело:'),
        ),
        migrations.AddField(
            model_name='blog',
            name='program_name_en',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Programm name:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='program_name_hy',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Ծրագրի անուն:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='program_name_ru',
            field=models.CharField(db_index=True, default='', max_length=200, verbose_name='Имя программы:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='author_en',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Author:'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author_hy',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Հեղինակ:'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author_ru',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Автор:'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='author_en',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Author:'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='author_hy',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Հեղինակ:'),
        ),
        migrations.AlterField(
            model_name='programs',
            name='author_ru',
            field=models.CharField(blank=True, db_index=True, max_length=50, verbose_name='Автор:'),
        ),
    ]
