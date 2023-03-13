from django.db import models


class Teacher(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    subject = models.CharField(max_length=10, verbose_name='Предмет')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Имя')
    teachers = models.ManyToManyField(Teacher, related_name='students', through='TeacherStudent')
    group = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ['group']

    def __str__(self):
        return self.name


class TeacherStudent(models.Model):
    id = models.BigAutoField(primary_key=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_student', verbose_name='Учителя')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='teacher_student', verbose_name='Учитель')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя учеников'
        default_related_name = 'teacher_student'
