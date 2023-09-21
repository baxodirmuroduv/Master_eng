from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, FormView
from django.views.generic.edit import DeleteView, UpdateView

from apps.forms import RegisterForm, StudentForm, GroupsForm
from apps.models import Register, Student, Groups


# class RegisterView(FormView):
#     template_name = 'register.html'
#     queryset = Register.objects.all()
#     form_class = RegisterForm
#     success_url = reverse_lazy('login')
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)
#
#
# class SignInView(LoginView):
#     next_page = reverse_lazy('home')
#     template_name = 'login.html'
#     redirect_authenticated_user = True


def register_page(request):
    if request.POST:
        data = RegisterForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('login')
        if errors := data.errors:
            print(errors.as_json(escape_html=True))
            return render(request, 'register.html', {'errors': errors})
    return render(request, 'register.html')


def login_page(request):
    data = request.POST
    if data:
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


# def save_view(request, pk):
#     if Register.objects.filter(id=pk):
#         user = request.user
#         if user.is_anonymous:
#             return redirect('login')
#         if request.POST:
#             form = RegisterForm(request.POST, files=request.FILES, instance=request.user)
#             if form.is_valid():
#                 form.save()
#     return render(request, 'index.html')


class HomeView(ListView):
    template_name = 'index.html'
    model = Groups
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        return context


class GroupView(CreateView):
    template_name = 'add_group.html'
    queryset = Groups.objects.all()
    form_class = GroupsForm
    success_url = reverse_lazy('home')


class GroupDelete(DeleteView):
    queryset = Groups.objects.all()
    template_name = 'student_list.html'
    success_url = reverse_lazy('home')


class GroupDetailView(ListView):
    model = Student
    template_name = 'student_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = Student.objects.all()
        pk = self.request.resolver_match.kwargs.get('pk')
        if pk:
            context["group"] = Groups.objects.filter(pk=pk).first()
        return context


class StudentView(CreateView):
    template_name = 'add_student.html'
    queryset = Student.objects.all()
    form_class = StudentForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = Groups.objects.all()
        pk = self.request.resolver_match.kwargs.get('pk')
        if pk:
            context["gr"] = Groups.objects.filter(pk=pk).first()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)


class ProfileDetailView(DetailView):
    template_name = 'profile_detail.html'
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.resolver_match.kwargs.get('pk')
        if pk:
            context["student"] = Student.objects.filter(pk=pk).first()
        return context


class StudentDelete(DeleteView):
    queryset = Student.objects.all()
    template_name = 'profile_detail.html'
    success_url = reverse_lazy('home')


class StudentUpdateView(UpdateView):
    queryset = Student.objects.all()
    # fields = '__all__'
    form_class = StudentForm
    template_name = 'profile_detail.html'
    success_url = reverse_lazy('home')
