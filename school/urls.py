from django.urls import path
from school import views

app_name = 'school'

urlpatterns = [

    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('login/', views.sign_in, name="sign_in"),
    path('logout/', views.sign_out, name="sign_out"),
    path('register/', views.register, name="register"),

    path('students/', views.all_students, name="students"),
    path('student/add/', views.add_student, name="add_student"),
    path('student/<int:sid>/edit/', views.edit_student, name="edit_student"),
    path('student/<int:sid>/delete/', views.delete_student, name="delete_student"),

    path('teachers/', views.all_teachers, name="teachers"),
    path('teacher/add', views.add_teacher, name="add_teacher"),
    path('teacher/<int:tid>/edit/', views.edit_teacher, name="edit_teacher"),
    path('teacher/<int:tid>/delete/', views.delete_teacher, name="delete_teacher"),

    path('courses/', views.all_courses, name="courses"),
    path('course/add', views.add_course, name="add_course"),
    path('course/<int:cid>/edit/', views.edit_course, name='edit_course'),
    path('course/<int:cid>/delete/', views.delete_course, name='delete_course'),

]
