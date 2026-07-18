from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        AGENT = "AGENT", "Agent"
        USER = "USER", "User"

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)

    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER,
    )

    is_verified = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
