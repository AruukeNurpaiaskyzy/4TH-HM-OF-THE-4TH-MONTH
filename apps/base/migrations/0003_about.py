# Generated by Django 5.1 on 2024-08-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_index_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='О нашем проекте')),
                ('description', models.TextField(verbose_name='Описание сайта ()')),
            ],
        ),
    ]
