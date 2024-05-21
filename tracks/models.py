from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Tracks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    image = models.ImageField(upload_to='tracks_images', blank=True, null=True, verbose_name='Изображение')
    audio_file = models.FileField(upload_to='tracks/', verbose_name='Аудиофайл', blank=True, null=True)
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name='Рейтинг трека'
    )
    categories = models.ManyToManyField(to='Categories', verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("сategories:track", kwargs={"track_slug": self.slug})

    class Meta:
        db_table = 'track'
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'
        ordering = ("id", )


