# Generated by Django 4.1.7 on 2023-03-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20230309_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scope',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tagsnews',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='headeng',
            field=models.ManyToManyField(related_name='articles', through='articles.Scope', to='articles.tagsnews'),
        ),
        migrations.AddField(
            model_name='tagsnews',
            name='name',
            field=models.CharField(default='Разное', max_length=50, verbose_name='Тег'),
        ),
    ]