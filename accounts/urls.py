from django.urls import path
from . import views

urlpatterns = [
    path('ssh/', views.ssh_users_view),
    path('ssh/create/', views.ssh_create_view),
    path('ssh/delete/', views.ssh_delete_view),
]