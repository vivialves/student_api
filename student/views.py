# -*- coding: utf-8 -*-

from rest_framework import generics

from .models import Responsible, Student
from .serializers import ResponsibleSerializer, StudentSerializer


class ResponsiblesAPIView(generics.ListCreateAPIView):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer

class ResponsibleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer

class StudentsAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

