from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    ResponsibleAPIView,
    ResponsiblesAPIView,
    StudentAPIView,
    StudentsAPIView)

router = SimpleRouter()
router.register('responsibles', ResponsibleAPIView)
router.register('students', StudentAPIView)

urlpatterns = [
    path('responsibles/', ResponsiblesAPIView.as_view(), name='responsibles'),
    path('responsible/<int:pk>/', ResponsibleAPIView.as_view(), name='student'),

    path('students/', StudentsAPIView.as_view(), name='students'),
    path('student/<int:pk>/', StudentAPIView.as_view(), name='student'),

]