from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.

def students_detail(request):
    students =[
        #{"id" : 1,"name" : "john","roll_number" : 1,"date_of_birth" :"11/3/2002","email" : "john@gmail.com","phone_number" : 234456,"address" : "rajkot"},
        #{"id" : 2,"name" : "jini","roll_number" : 2,"date_of_birth" :"10/5/2002","email" : "jini@gmail.com","phone_number" : 23345456,"address" : "bhuj"},
        #{"id" : 3,"name" : "rohan","roll_number" : 3,"date_of_birth" :"8/9/2002","email" : "rohan@gmail.com","phone_number" : 23789656,"address" : "ahmedabad"},
    ] 
    students = Student.objects.all()
    return render(request,"student.html",{"students" :students})

def student_insert(request):
    return render(request,"student_insert.html")

def insert_save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_number')
        birth = request.POST.get('date_birth')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        students = Student(name = name,roll_number = roll_no,date_of_birth = birth,email = email,phone_number = phone,address = address)
        students.save()

        messages.success(request,"student inserted successfully")
        return redirect('/students/')
    
def student_edit(request,student_id):
    students = Student.objects.get(pk = student_id)
    return render(request,'student_update.html',{"students": students})    

def student_updated(request,student_id):
    if request.method == "POST":
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_number')
        birth = request.POST.get('date_birth')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        students = Student.objects.get(pk = student_id)
        students.name = name
        students.roll_number = roll_no
        students.date_of_birth = birth
        students.email = email
        students.phone_number = phone
        students.address = address
        students.save()

        messages.success(request,"record updated successfuly")
        return redirect("/students/")
    
def student_delete(request,student_id):
    students = Student.objects.filter(pk = student_id)
    students.delete()
    messages.success(request,"record deleted successfuly")
    return redirect("/students/")
    
def student_all_detail(request,student_id):
    student = Student.objects.get(pk = student_id)
    return render(request,"student_detail.html",{"student" : student})



