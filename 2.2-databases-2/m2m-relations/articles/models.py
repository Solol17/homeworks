from django.db import models
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class MainCategoryArticles(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article_categories')
    is_main = models.BooleanField(default=False, verbose_name='Основная категория')

    def clean(self):
        if self.is_main:
            existing_main = MainCategoryArticles.objects.filter(
                article=self.article,
                is_main=True
            ).exclude(pk=self.pk).exists()

            if existing_main:
                raise ValidationError('У статьи может быть только одна основная категория')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.article.title} - {self.tag.name}"