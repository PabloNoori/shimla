from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from . import plugins
import os
import crypt

# Create your views here.

@login_required
def group_view(request):
    return render(request, 'theme-i/pages/accounts/accounts.html')

@login_required
def ssh_users_view(request):
    context = {
        'ssh_accounts': models.SSH_accounts.objects.all(),
        'check_root': plugins.check_root(),
        'is_linux': plugins.is_linux()
    }
    return render(request, 'theme-i/pages/accounts/ssh/users.html', context=context)

@login_required
def ssh_create_view(request):
    form = forms.SSHForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        ucrypt=crypt.crypt(password,"123")
        os.system("sudo useradd -p {} -m {} -s /bin/true".format(ucrypt, username))
        return redirect('accounts:ssh')
    
    context = {
        'form': form
    }
    return render(request, 'theme-i/pages/accounts/ssh/create.html', context=context)

@login_required
def ssh_delete_view(request, pk):
    get_user = models.SSH_accounts.objects.get(pk=pk)
    print(get_user)
    os.system("killall -u {}".format(get_user))
    os.system("userdel {} -r".format(get_user))
    get_user.delete()
    return redirect('accounts:ssh')
