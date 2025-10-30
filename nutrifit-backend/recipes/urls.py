from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, IngredientViewSet, RecipeViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = router.urls
