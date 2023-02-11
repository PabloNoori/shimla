from django.shortcuts import render
import os
import crypt

# Create your views here.

def group_view(request):
    return render(request, 'theme-i/pages/accounts/group.html')

def ssh_users_view(request):
    return render(request, 'theme-i/pages/accounts/ssh/users.html')

def ssh_create_view(request):
    password = "p@ssw0rd"
    encPass = crypt.crypt(password, "22")
    os.system("useradd -p "+encPass+" alii")
    return render(request, 'theme-i/pages/home.html')

def ssh_delete_view(request):
    os.system("userdel alii")
    return render(request, 'theme-i/pages/home.html')
