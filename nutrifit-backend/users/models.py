from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="email address")


class Profile(models.Model):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "O", "Other"

    class ActivityLevel(models.TextChoices):
        LOW = "L", "Low"
        MEDIUM = "M", "Medium"
        HIGH = "H", "High"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    goal = models.TextField(blank=True, null=True, verbose_name="Goal")
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Weight")
    height = models.PositiveIntegerField(blank=True, null=True, verbose_name="Height")
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Age")
    gender = models.CharField(max_length=1, choices=Gender.choices, blank=True, null=True, verbose_name="Gender")

    activity_level = models.CharField(max_length=1, choices=ActivityLevel.choices, default=ActivityLevel.LOW,
                                      blank=True, null=True,
                                      verbose_name="Activity level")

    def __str__(self):
        return f"{self.user.username}'s profile"