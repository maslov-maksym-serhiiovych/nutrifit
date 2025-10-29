from django.db import models
from django.db.models import Sum, F


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category name")
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Ingredient name")
    calories = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    carbs = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Carbohydrates")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, verbose_name="Recipe name")
    description = models.TextField(blank=True, verbose_name="Recipe description")
    instructions = models.TextField(verbose_name="Recipe instructions")
    prep_time = models.PositiveIntegerField(verbose_name="Recipe prep time")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="recipes",
                                 verbose_name="Recipe category")

    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', verbose_name="Recipe ingredients")
    total_calories = models.PositiveIntegerField(default=0, verbose_name='Total calories')

    def update_total_calories(self):
        aggregation = self.recipeingredient_set.aggregate(
            calculated_total=Sum(F('ingredient__calories') / 100 * F('amount'),
                                 output_field=models.DecimalField())
        )

        self.total_calories = round(aggregation.get('calculated_total') or 0)

        self.save(update_fields=['total_calories'])

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ingredient amount")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.recipe.update_total_calories()

    def delete(self, *args, **kwargs):
        recipe = self.recipe
        super().delete(*args, **kwargs)
        recipe.update_total_calories()

    class Meta:
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return f"{self.ingredient.name} in {self.recipe.name}"
