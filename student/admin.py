# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Position, Employee, Responsible, Student

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'status')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name',
                    'doc_number',
                    'address',
                    'city',
                    'state',
                    'timestamp_created',
                    'status',
                    'position')

@admin.register(Responsible)
class ResponsibleAdmin(admin.ModelAdmin):
    list_display = ('full_name',
                    'doc_number',
                    'address',
                    'city',
                    'state',
                    'timestamp_created',
                    'status',
                    'email',
                    'phone_number',
                    'employee')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name',
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
                    'employee')

