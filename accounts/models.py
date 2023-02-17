from django.db import models

# Create your models here.


class SSH_accounts(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'SSH Accounts'
        verbose_name = 'SSH Accounts'

    def __str__(self):
      return self.username
