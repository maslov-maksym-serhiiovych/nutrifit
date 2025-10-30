from rest_framework import serializers
from .models import Exercise, Workout, WorkoutExercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise_name = serializers.CharField(source='exercise.name', read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ('exercise', 'exercise_name', 'sets', 'reps', 'weight')


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = WorkoutExerciseSerializer(source='workoutexercise_set', many=True, read_only=True)
    owner_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Workout
        fields = ('id', 'user', 'owner_username', 'name', 'workout_type', 'created_at', 'exercises')
        read_only_fields = ('user',)
