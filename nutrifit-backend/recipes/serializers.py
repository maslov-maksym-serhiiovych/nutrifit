from rest_framework import serializers
from .models import Category, Ingredient, Recipe, RecipeIngredient


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.CharField(source='ingredient.name', read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'ingredient_name', 'amount')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True, read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Recipe

        fields = ('id', 'name', 'description', 'instructions', 'prep_time', 'category', 'category_name', 'ingredients',
                  'total_calories')

        read_only_fields = ('total_calories',)

