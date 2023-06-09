from django.contrib import admin
from .models import Student, Teacher, Principal, ExamCenter, Candidate, MyExamCenter


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'roll']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'date', 'salary']


@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'experience', 'date']


@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city', 'roll']


@admin.register(MyExamCenter)
class MyExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'city']
