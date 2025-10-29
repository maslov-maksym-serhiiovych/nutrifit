from django.contrib import admin
from .models import Exercise, Workout, WorkoutExercise


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'workout_type', 'created_at')
    list_filter = ('workout_type', 'user')
    search_fields = ('name', 'user__username')
    inlines = [WorkoutExerciseInline]


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'muscle_group')
    list_filter = ('muscle_group',)
    search_fields = ('name',)
