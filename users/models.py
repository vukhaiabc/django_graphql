from django.db import models
from django.contrib.auth.models import AbstractUser
class UserCustom(AbstractUser) :
    email = models.EmailField(blank=False,max_length=255,verbose_name='email')

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username