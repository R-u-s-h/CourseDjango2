from django.db import models

class Category(models.Model):
    """Модель категорий"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    """Модель тэгов"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)

class Post(models.Model):
    """Модель постов"""
    title = models.CharField("Имя", max_length=100)
    mini_text = models.TextField()
    text = models.TextField()
    created_date = models.DateTimeField()
    slug = models.SlugField("url", max_length=100)

class Comment(models.Model):
    """Модель комментариев"""
    text = models.TextField()
    created_date = models.DateTimeField()
    moderation = models.BooleanField()