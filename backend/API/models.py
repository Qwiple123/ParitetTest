from django.db import models




class Image(models.Model):
    image = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f"{self.description}"