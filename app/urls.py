from django.urls import path, include
from app.views import StudentModelViewSet, TeacherModelViewSet, PrincipalModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student', StudentModelViewSet, basename='student')
router.register('teacher', TeacherModelViewSet, basename='teacher')
router.register('principle', PrincipalModelViewSet, basename='principle')

urlpatterns = [
    path('', include(router.urls)),
]
