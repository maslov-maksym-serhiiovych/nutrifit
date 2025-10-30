from django.db import models
from django.conf import settings
from django.utils import timezone


class WeightLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='weight_logs')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(default=timezone.now, verbose_name='Log date')

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg ({self.date})"


class CalorieLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='calorie_logs')
    calories_consumed = models.PositiveIntegerField(verbose_name='Consumed calories')
    date = models.DateField(default=timezone.now, verbose_name='Log date')

    class Meta:
        unique_together = ('user', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.calories_consumed} ccal ({self.date})"
