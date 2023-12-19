from django.db import models

# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    continent = models.CharField(max_length=30, verbose_name='Континент')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    students_quantity = models.IntegerField(verbose_name='Количество студентов')
    built_in = models.IntegerField(verbose_name='Год основания')
    test_type = models.CharField(max_length=30, verbose_name='Тип теста по английскому языку')
    test_score = models.IntegerField(verbose_name='Требуемый балл')
    acceptance_age = models.IntegerField(verbose_name='Возраст')
    live_type = models.CharField(max_length=30, verbose_name='Тип проживания')
    faculty_quantity = models.IntegerField(verbose_name='Количество факультетов')
    short_detail = models.CharField(max_length=150, verbose_name='Краткие подробности')
    body = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    age = models.IntegerField()
