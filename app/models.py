from django.db import models


# Abstract class
class Common(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Student(Common):
    roll = models.IntegerField()
    date = None


class Teacher(Common):
    salary = models.IntegerField()


class Principal(Common):
    experience = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


# Multitable Inheritance
class ExamCenter(models.Model):
    city = models.CharField(max_length=30)


class Candidate(ExamCenter):
    name = models.CharField(max_length=35)
    roll = models.IntegerField()


# Proxy Model
class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True
        ordering = ['id']
