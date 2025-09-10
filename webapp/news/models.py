from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Articles(models.Model):

    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField()
    date = models.DateTimeField('Дата публикации')
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'news'