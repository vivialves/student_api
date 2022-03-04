# -*- coding: utf-8 -*-

from django.db import models


class Base(models.Model):
    """
    Data in common in other table
    """
    full_name = models.CharField(max_length=255)
    doc_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    timestamp_created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Position(models.Model):
    """
    Employee position
    """
    position_name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.position_name


class Employee(Base):
    """
    Data from Employee that fill student data and responsible data
    """

    position = models.ForeignKey(Position, related_name='position', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name

class Responsible(Base):
    """
    Data from responsible of students
    """

    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    employee = models.ForeignKey(Employee, related_name='employee_r', on_delete=models.CASCADE)
    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name

class Student(Base):
    """
    Data from student
    """

    UNDEFINED = ''
    MALE = 'M'
    FEMALE = 'F'
    SEX = (
        (UNDEFINED, ''),
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE')
    )

    MOTHER = 'M'
    FATHER = 'F'
    OTHER = 'O'
    RESPONSIBLE_TYPES = (
        (OTHER, 'O'),
        (MOTHER, 'M'),
        (FATHER, 'F')
    )
    
    
    birth_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX, blank=True, default=UNDEFINED, help_text='M - Male | F - Female')
    email = models.EmailField(blank=True)
    responsible = models.ForeignKey(Responsible, related_name='responsible', on_delete=models.CASCADE)
    responsible_type = models.CharField(max_length=1, choices=RESPONSIBLE_TYPES, help_text='M - Mother | F - Father | O - Other')
    employee = models.ForeignKey(Employee, related_name='employee_s', on_delete=models.CASCADE)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name
