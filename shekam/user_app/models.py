from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    class Meta:
        db_table = 'users'
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

