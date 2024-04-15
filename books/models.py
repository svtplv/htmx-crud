from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.CharField(max_length=200, verbose_name='Автор')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    read = models.BooleanField(default=False, verbose_name='Прочтено')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
