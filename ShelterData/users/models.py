from django.db import models
from django.contrib.auth.models import AbstractUser


class SDUser(AbstractUser):
    

    def __str__(self) -> str:
        return self.username




# Create your models here.
