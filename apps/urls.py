from django.urls import path

from apps.views import RegisterView, SignInView, StudentView, HomeView, GroupdetailView, GroupView, ProfileDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('group_detail/<int:pk>/', GroupdetailView.as_view(), name='group_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('add/', StudentView.as_view(), name='add'),
    path('add_new_group/', GroupView.as_view(), name='add_new_group'),
]
