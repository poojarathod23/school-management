from django.contrib import admin
from school.models import Student, Teacher, Course

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)