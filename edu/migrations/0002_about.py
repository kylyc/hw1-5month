# Generated by Django 4.2.8 on 2023-12-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photoshop', models.CharField(max_length=155, verbose_name='Фотошоп')),
                ('Indesign', models.CharField(max_length=155, verbose_name='Индизайн')),
                ('Web_Programing', models.CharField(max_length=155, verbose_name='Веб-программирование')),
                ('Adobe_Illustrator', models.CharField(max_length=155, verbose_name='Adobe-Illustrator')),
            ],
            options={
                'verbose_name': 'Обо мне',
                'verbose_name_plural': 'Обо мне',
            },
        ),
    ]
