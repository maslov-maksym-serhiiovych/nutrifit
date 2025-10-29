from django.contrib import admin
from .models import Category, Ingredient, Recipe, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'prep_time', 'total_calories')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [RecipeIngredientInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'protein', 'fat', 'carbs')
    search_fields = ('name',)


admin.site.register(Category)
