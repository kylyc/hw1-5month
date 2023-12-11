from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок-1',
        blank=True, null=True
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name='ЗАголовка-2',
        blank=True, null=True
    )
    descriptions = models.CharField(
        max_length=300,
        verbose_name='Описание',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='settings',
        verbose_name='Фото',
        blank=True, null=True
    )
    title3 = models.CharField(
        max_length=255,
        verbose_name='ЗАголовка-3',
        blank=True, null=True
    )
    descriptions2 = models.TextField(
        verbose_name='Описание2',
        blank=True, null=True
    )
    services_title = models.CharField(
        max_length=255,
        verbose_name='ЗАголовок услуги ',
        blank=True, null=True
    )
    title4 = models.CharField(
        max_length=255,
        verbose_name='ЗАголовка-4',
        blank=True, null=True
    )
    descriptions3 = models.TextField(
        verbose_name='Описание3',
        blank=True, null=True
    )

    def __str__(self):
        return self.title4

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройка главной строницы"

class Portfolio(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="ЗАголовка"
    )
    descriptions = models.TextField(
        verbose_name='Описание',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройка"

class Work(models.Model):
    services_title = models.CharField(
        max_length=155,
        verbose_name="Заголовок услуги"
    )
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='Work',
        verbose_name='Фото'
    )
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройка2"

class Clients(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    descriptions = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='Work',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройка3"

class Info(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name="Заголовка"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Телефонный номер"
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Настройка4"