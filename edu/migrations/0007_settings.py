# Generated by Django 4.2.8 on 2023-12-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0006_rename_awesome_services_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовок-1')),
                ('title2', models.CharField(max_length=255, verbose_name='ЗАголовка-2')),
                ('descriptions', models.CharField(max_length=300, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='settings', verbose_name='Фото')),
                ('title3', models.CharField(max_length=255, verbose_name='ЗАголовка-3')),
                ('descriptions2', models.TextField(verbose_name='Описание2')),
                ('services_title', models.CharField(max_length=255, verbose_name='ЗАголовок - 4')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройка главной строницы',
            },
        ),
    ]