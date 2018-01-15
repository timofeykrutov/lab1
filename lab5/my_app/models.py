from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
        name_book = models.CharField(max_length=100)
        price_book = models.IntegerField(default=36)


class Writer (models.Model):
        writer_fio = models.CharField(max_length=100)
        writer_book = models.CharField(max_length=100)

class teacherIU(models.Model):
        teacher_fio = models.CharField(max_length=100)
        teacher_department = models.CharField(max_length=100)
        teacher_f = models.CharField(max_length=100)

class teacherSM(models.Model):
        teacher_fio = models.CharField(max_length=100)
        teacher_department = models.CharField(max_length=100)


class teacherRT(models.Model):
        teacher_fio = models.CharField(max_length=100)
        teacher_department = models.CharField(max_length=100)


class teacherBMT(models.Model):
        teacher_fio = models.CharField(max_length=100)
        teacher_department = models.CharField(max_length=100)

class students(models.Model):
    id_students = models.AutoField(primary_key=True)
    student_fio = models.CharField(max_length=100, blank=False, null=False, verbose_name='ФИО Студента')
    group_number = models.CharField(max_length=100, verbose_name='Номер группы')

    def __str__(self):
        return '%s' % (self.student_fio)

    # def natural_key(self):
    #     return '%s %s %s' % (self.hotell, self.kod_nomera, self.patronymic)

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"

class groups(models.Model):
    id_groups = models.AutoField(primary_key=True)
    group_number = models.CharField(max_length=45, verbose_name='Номер группы')
    faculty = models.ForeignKey(students, on_delete=models.CASCADE, verbose_name='Факультет')

    def __str__(self):
        return self.group_number

    class Meta:
        verbose_name_plural = "Группы"
        verbose_name = "Группа"


class teachers(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    teacher_fio = models.CharField(max_length=100, blank=False, null=False, verbose_name='ФИО преподавателя')
    teacher_department = models.CharField(max_length=100, verbose_name='Кафедра')
    group_num = models.ManyToManyField(groups, verbose_name='Номер группы')

    def __str__(self):
        return self.teacher_fio

    class Meta:
        verbose_name_plural = "Преподаватели"
        verbose_name = "Преподаватель"

    def get_group_num(self):
        return [r.group_number for r in self.group_num.all()]
    get_group_num.short_description = 'Номер группы'

