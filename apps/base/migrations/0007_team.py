# Generated by Django 5.1 on 2024-08-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_image_photo2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название тайтла')),
                ('description', models.TextField(verbose_name='Описание тайтла')),
            ],
            options={
                'verbose_name': 'название',
                'verbose_name_plural': 'названии',
            },
        ),
    ]
