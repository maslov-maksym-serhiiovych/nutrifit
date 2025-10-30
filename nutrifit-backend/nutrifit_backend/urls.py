from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import UserProfileViewSet
from recipes.views import CategoryViewSet, IngredientViewSet, RecipeViewSet
from workouts.views import ExerciseViewSet, WorkoutViewSet

router = DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='user-profile')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'exercises', ExerciseViewSet, basename='exercise')
router.register(r'workouts', WorkoutViewSet, basename='workout')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
