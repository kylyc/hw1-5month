# Generated by Django 4.2.8 on 2023-12-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0011_portfolio_delete_about_delete_infouser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_title', models.CharField(max_length=155, verbose_name='Заголовок услуги')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Work', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройка2',
            },
        ),
    ]