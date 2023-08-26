from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from apps.forms import RegisterForm, StudentForm, GroupsForm
from apps.models import Register, Student, Groups


class ProfileDetailView(DetailView):
    template_name = 'profile_detail.html'
    model = Student
    context_object_name = 'student'


class HomeView(ListView):
    template_name = 'index.html'
    model = Groups
    context_object_name = 'groups'


# class GroupdetailView(ListView):
#     template_name = 'student_list.html'
#     model = Student
#     context_object_name = 'students'


class GroupdetailView(ListView):
    model = Student
    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        pk = self.request.resolver_match.kwargs.get('pk')
        if pk:
            context["group"] = Groups.objects.filter(pk=pk).first()
        return context


class RegisterView(CreateView):
    template_name = 'register.html'
    queryset = Register.objects.all()
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class StudentView(CreateView):
    template_name = 'add_student.html'
    queryset = Student.objects.all()
    form_class = StudentForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = Groups.objects.all()
        return context


class GroupView(CreateView):
    template_name = 'add_group.html'
    queryset = Groups.objects.all()
    form_class = GroupsForm
    success_url = reverse_lazy('home')


class SignInView(LoginView):
    next_page = reverse_lazy('register')
    template_name = 'login.html'
    redirect_authenticated_user = True
