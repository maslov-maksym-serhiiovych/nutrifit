from rest_framework import viewsets, permissions
from .models import CustomUser
from .permissions import IsOwner
from .serializers import CustomUserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.all() if user.is_staff else CustomUser.objects.filter(pk=user.pk)
