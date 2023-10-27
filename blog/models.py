from django.db import models

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=20, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

