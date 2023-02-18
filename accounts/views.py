from django.shortcuts import render, redirect
from . import models
from . import forms
import os
import crypt

# Create your views here.

def group_view(request):
    return render(request, 'theme-i/pages/accounts/accounts.html')

def ssh_users_view(request):
    context = {
        'ssh_accounts': models.SSH_accounts.objects.all()
    }
    return render(request, 'theme-i/pages/accounts/ssh/users.html', context=context)

def ssh_create_view(request):
    form = forms.SSHForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        ucrypt=crypt.crypt(password,"123")
        os.system("sudo useradd -p {} -m {}".format(ucrypt, username))
        return redirect('accounts:ssh')
    
    context = {
        'form': form
    }
    return render(request, 'theme-i/pages/accounts/ssh/create.html', context=context)

def ssh_delete_view(request, pk):
    get_user = models.SSH_accounts.objects.get(pk=pk)
    print(get_user)
    os.system("killall -u {}".format(get_user))
    os.system("userdel {} -r".format(get_user))
    get_user.delete()
    return redirect('accounts:ssh')
