from django.db import models


class Writer(models.Model):
    name = models.CharField(verbose_name="Имя писателя", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Писатель'
        verbose_name_plural = 'Писатели'

    def __str__(self):
        return self.name

class Book(models.Model):
    name_book = models.CharField(verbose_name="Название произведения", max_length=100, null=True, blank=True)
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name_book
