from django.forms import ModelForm

from .models import Register, Student, Groups


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'
