from django import forms
from studentcrudapp.models import Student

class StudentForm(forms.ModelForm):
    class_list= [
    ('Class IIX', 'Class IIX'),
    ('Class IX', 'Class IX'),
    ('Class X', 'Class X'),
    ('Class XI', 'Class XI'),
    ('Class XII', 'Class XII')
    ]
    student_class= forms.CharField(label='Class', widget=forms.Select(choices=class_list,attrs={'style': 'width:175px'}))
    class Meta:
        model=Student
        #To add selective fields you can give it as
        #fields=('student_id',student_name)
        #since we need all fields we use '__all__'
        fields='__all__'
        #fields=('student_name',)