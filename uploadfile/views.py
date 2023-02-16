from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import UploadFileForm  
from .models import Student

# Create your views here.
def index(request):
    return render(request,"uploadfile/index.html")

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(str(request.FILES['file']))
            stu = Student(name = str(request.POST['name_student']),grade = str(request.POST['grade_student']),file_student = str(request.FILES['file']))
            stu.save()
            return HttpResponseRedirect(reverse_lazy("uploadfile:success"))
        # return HttpResponse("Sucess")
    else:
        form = UploadFileForm()
    return render(request, "uploadfile/upload.html", {'form':form})


def results(request):
    students_list = Student.objects.order_by('-name')
    return render(request, 'uploadfile/results.html',{'students_list':students_list})

def success(request):
    return render(request, 'uploadfile/success.html')

# def download(request,student_id):
#     student = get_object_or_404(Student, pk = student_id)
#     with open(f'Content/{str(student.file_student).split(".")[0]}.txt','wb+') as f:
#         for chunk in student.file_student.chunks():
#             f.write(chunk)


def contents(request,student_id):
    student = get_object_or_404(Student, pk = student_id)
    content = ""
    print('student',student.file_student)
    for chunk in student.file_student.chunks():
        content += chunk.decode('UTF-8')
    return render(request, 'uploadfile/content.html',{'contents':content})
    
