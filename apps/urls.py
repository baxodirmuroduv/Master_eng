from django.urls import path

from apps.views import StudentView, HomeView, GroupDetailView, GroupView, ProfileDetailView, \
    GroupDelete, StudentDelete, StudentUpdateView, register_page, login_page

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('group_detail/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    path('group_delete/<int:pk>/', GroupDelete.as_view(), name='delete'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('add/<int:pk>', StudentView.as_view(), name='add'),
    path('add_new_group/', GroupView.as_view(), name='add_new_group'),
    path('student_delete/<int:pk>/', StudentDelete.as_view(), name='student_delete'),
    path('student_update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),

]
