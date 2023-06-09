from rest_framework import serializers
from .models import Student, Teacher, Principal


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'roll']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'age', 'date', 'salary']


class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = ['id', 'name', 'age', 'experience', 'date']
