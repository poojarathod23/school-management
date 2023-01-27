from django.forms import ModelForm
from school.models import Teacher, Student, Course

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'