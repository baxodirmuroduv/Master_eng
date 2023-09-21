from django.forms import ModelForm

from .models import Register, Student, Groups


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = 'name', 'username', 'email', 'password'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = 'create_at',


class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'
