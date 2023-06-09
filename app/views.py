from .models import Student, Teacher, Principal
from .serializers import StudentSerializer, TeacherSerializer, PrincipalSerializer
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class PrincipalModelViewSet(viewsets.ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = TeacherSerializer
