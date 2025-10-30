from rest_framework import serializers
from .models import WeightLog, CalorieLog


class WeightLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightLog
        fields = ('id', 'weight', 'date')


class CalorieLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieLog
        fields = ('id', 'calories_consumed', 'date')
