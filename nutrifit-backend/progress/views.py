from rest_framework import viewsets, permissions
from .models import WeightLog, CalorieLog
from .serializers import WeightLogSerializer, CalorieLogSerializer


class BaseProgressViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WeightLogViewSet(BaseProgressViewSet):
    queryset = WeightLog.objects.all()
    serializer_class = WeightLogSerializer


class CalorieLogViewSet(BaseProgressViewSet):
    queryset = CalorieLog.objects.all()
    serializer_class = CalorieLogSerializer
