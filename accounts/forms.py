from django.forms import ModelForm
from . import models

class SSHForm(ModelForm):
    class Meta:
        model = models.SSH_accounts
        fields = ('username', 'password')