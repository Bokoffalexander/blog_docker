from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название поста")
    content = models.TextField(blank=True, verbose_name="Содержание поста")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания поста")
    is_published = models.BooleanField(verbose_name="Опубликован ли пост")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Имя владельца поста")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['time_create']
        verbose_name_plural = "Посты"
