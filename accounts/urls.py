from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.group_view , name='home'),
    path('ssh/', views.ssh_users_view, name='ssh'),
    path('ssh/create/', views.ssh_create_view, name='ssh_create'),
    path('ssh/delete/', views.ssh_delete_view, name='ssh_delete'),
]