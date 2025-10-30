from rest_framework import viewsets
from .models import Category, Ingredient, Recipe
from .serializers import CategorySerializer, IngredientSerializer, RecipeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().prefetch_related('recipeingredient_set__ingredient', 'category')
    serializer_class = RecipeSerializer
