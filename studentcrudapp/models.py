from django.db import models

# Create your models here.

class Student(models.Model):
    student_id=models.CharField(max_length=20)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField()
    student_contact=models.CharField(max_length=100)
    student_class=models.CharField(max_length=100)
    class Meta:
        db_table='student'
