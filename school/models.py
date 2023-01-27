from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)
    salary = models.IntegerField()

    def __str__(self) -> str:
        return self.teacher_name


class Student(models.Model):
    student_name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    fees = models.IntegerField()

    def __str__(self) -> str:
        return self.student_name


class Course(models.Model):
    course_name = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)
    budget = models.IntegerField()

    def __str__(self) -> str:
        return self.course_name
