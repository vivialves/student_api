# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Responsible, Student


class ResponsibleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Responsible
        fields = (
            'id',
            'full_name',
            'doc_number',
            'address',
            'city',
            'state',
            'timestamp_created',
            'status',
            'email',
            'phone_number',
            'employee'
        )

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = (
            'id',
            'full_name',
            'doc_number',
            'address',
            'city',
            'state',
            'timestamp_created',
            'status',
            'birth_date', 
            'sex', 
            'email', 
            'responsible', 
            'responsible_type', 
            'employee'
        )

