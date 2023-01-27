from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from school.models import Teacher, Student, Course
from school.forms import TeacherForm, StudentForm, CourseForm

# Create your views here.

def register(request):

    if request.user.is_authenticated:
            return redirect('/school/index')

    if request.method == "POST":
        try:
            user = User()
            user.first_name = request.POST.get('fname')
            user.last_name = request.POST.get('lname')
            user.email = request.POST.get('email')
            user.username = request.POST.get('uname')
            user.password = make_password(request.POST.get('passwd'))
            user.save()
            messages.add_message(request, messages.SUCCESS, "Account created successfully, sign in to continue!")
            return redirect('/school/login')
        except IntegrityError:
            messages.add_message(request, messages.ERROR, "Username is alredy taken!")
    return render(request,'register.html')

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        user = authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return redirect('/school/index/')
        else:
            messages.add_message(request, messages.ERROR, "Incorrect username or password!")
    else:
        try:
            if request.user.is_authenticated:
                return redirect('/school/index')
        except Exception as e:
            messages.add_message(request, messages.ERROR, str(e))
    return render(request,'login.html')

@login_required(login_url='/school/login/')
def sign_out(request):
    logout(request)
    return redirect("/school/login/")


@login_required(login_url='/school/login/')
def index(request):

    return render(request, 'index.html')


@login_required(login_url='/school/login/')
def all_students(request):

    students = Student.objects.all()

    return render(request, 'students.html', {'students': students})


@login_required(login_url='/school/login/')
def add_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/school/students/')
    return render(request, 'add_student.html', {'form': form})


@login_required(login_url='/school/login/')
def edit_student(request, sid):

    student = get_object_or_404(Student, pk=sid)

    if request.method == 'POST':
        sname = request.POST.get('student_name')
        course = request.POST.get('course')
        fees = request.POST.get('fees')

        student.student_name = sname
        student.course = course
        student.fees = fees

        student.save()

        return redirect('/school/students/')

    return render(request, 'edit_student.html', {'student': student})


@login_required(login_url='/school/login/')
def delete_student(request, sid):

    student = get_object_or_404(Student, pk=sid)

    if student:
        student.delete()

    return redirect('/school/students/')


@login_required(login_url='/school/login/')
def all_teachers(request):

    teachers = Teacher.objects.all()

    return render(request, 'teachers.html', {'teachers': teachers})


@login_required(login_url='/school/login/')
def add_teacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/school/teachers/')
    return render(request, 'add_teacher.html', {'form': form})


@login_required(login_url='/school/login/')
def edit_teacher(request, tid):

    teacher = get_object_or_404(Teacher, pk=tid)

    if request.method == 'POST':
        tname = request.POST.get('teacher_name')
        dept = request.POST.get('dept')
        sal = request.POST.get('salary')

        teacher.teacher_name = tname
        teacher.dept = dept
        teacher.salary = sal

        teacher.save()

        return redirect('/school/teachers/')

    return render(request, 'edit_teacher.html', {'teacher': teacher})


@login_required(login_url='/school/login/')
def delete_teacher(request, tid):

    teacher = get_object_or_404(Teacher, pk=tid)

    if teacher:
        teacher.delete()

    return redirect('/school/teachers/')


@login_required(login_url='/school/login/')
def all_courses(request):

    courses = Course.objects.all()

    return render(request, 'courses.html', {'courses': courses})


@login_required(login_url='/school/login/')
def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/school/courses/')
    return render(request, 'add_course.html', {'form': form})


@login_required(login_url='/school/login/')
def edit_course(request, cid):

    course = get_object_or_404(Course, pk=cid)

    if request.method == 'POST':
        cname = request.POST.get('course_name')
        dept = request.POST.get('dept')
        budget = request.POST.get('budget')

        course.course_name = cname
        course.dept = dept
        course.budget = budget

        course.save()

        return redirect('/school/courses/')

    return render(request, 'edit_course.html', {'course': course})


@login_required(login_url='/school/login/')
def delete_course(request, cid):

    course = get_object_or_404(Course, pk=cid)

    if course:
        course.delete()
        messages.add_message(request, messages.SUCCESS, "Account created successfully, sign in to continue!")

    return redirect('/school/courses/')