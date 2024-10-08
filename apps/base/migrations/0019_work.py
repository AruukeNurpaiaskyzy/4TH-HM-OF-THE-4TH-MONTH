# Generated by Django 5.1 on 2024-08-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_navigation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название работы')),
                ('description', models.TextField(verbose_name='описание работы')),
                ('image', models.ImageField(upload_to='jobs', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'работы',
            },
        ),
    ]
