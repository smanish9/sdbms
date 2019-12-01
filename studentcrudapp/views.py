from django.shortcuts import render,redirect
from django.http import HttpResponse
from studentcrudapp.forms import StudentForm
from studentcrudapp.models import Student


def index(request):
    students = Student.objects.all()
    for i in students:
        print(i)
    return render(request,'stdntcrudtmpl/index.html',{'students':students})

def about(request):
    return render(request,'stdntcrudtmpl/about.html')  

def student(request):
    print('inside post')
    if request.method=='POST':
        print('inside post11')
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                print('inside posting try')
                form.save()
                return redirect('/')
            except:
                print('some error')
                form.errors()
    else:
        print('here in the else')
        form=StudentForm()
    return render(request,"stdntcrudtmpl/student.html",{'form':form})

def edit(request,id):
    student = Student.objects.get(id=id)
    form=StudentForm(instance=student)
    return render(request,"stdntcrudtmpl/editstudent.html",{'student':student,'form':form})

def update(request,id):
    student = Student.objects.get(id=id)
    form=StudentForm(request.POST,instance=student)
    print('inside update')
    if form.is_valid():
        try:
            print('inside update try')
            form.save()
            return redirect('/')
        except:
            print('update error')
            print(form.errors)
    return render(request,"stdntcrudtmpl/editstudent.html",{'student':student}) 

def delete(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')