from django.db import models
from django.conf import settings


class Exercise(models.Model):
    class MuscleGroup(models.TextChoices):
        CHEST = 'CH', "Chest"
        BACK = 'BK', "Back"
        LEGS = 'LG', "Legs"
        SHOULDERS = 'SH', "Shoulders"
        ARMS = 'AR', "Arms"
        CORE = 'CO', "Core"
        FULL_BODY = 'FB', "Full body"
        CARDIO = 'CA', "Cardio"

    name = models.CharField(max_length=200, verbose_name='Exercise name')
    description = models.TextField(blank=True, verbose_name='Description')
    muscle_group = models.CharField(max_length=2, choices=MuscleGroup.choices, verbose_name='Target muscle group')

    def __str__(self):
        return self.name


class Workout(models.Model):
    class WorkoutType(models.TextChoices):
        STRENGTH = 'ST', 'Strenght'
        CARDIO = 'CA', 'Cardio'
        HYBRID = 'HY', 'Hybrid'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=200, verbose_name='Workout name')
    workout_type = models.CharField(max_length=2, choices=WorkoutType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField(verbose_name='Repetitions')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Weight')

    class Meta:
        unique_together = ('workout', 'exercise')

    def __str__(self):
        return f"{self.exercise.name} in {self.workout.name}"
