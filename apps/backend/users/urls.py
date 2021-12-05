from django.urls import path, include
from .views import *
from django.views.generic import TemplateView, RedirectView

app_name = 'backend.users'
urlpatterns = [
    path('users/', IndexUserView.as_view(), name='index'),
    path('users/register/', UserRegistrationField.as_view(), name='create'),
    path('users/edit/<str:pk>/', UpdateUserView.as_view(), name='edit'),
    path('users/delete/<str:pk>/', DeleteUserView.as_view(), name='delete'),
    path('login/', UserLoginField.as_view(), name='login'),
    path('logout/', UserLogoutField.as_view(), name='logout'),
]
