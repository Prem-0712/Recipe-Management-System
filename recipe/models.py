from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):

    CATEGORIES = (
        ('appetizers and snack', 'APPETIZERS AND SNACK'),
        ('main dishes', 'MAIN DISHES'),
        ('bread and blaked goods', 'BREAD AND BLAKED GOODS'),
        ('desserts', 'DESSERTS'),
        ('salads and slides', 'SALADS AND SLIDES'),
        ('soups and stews', 'SOUPS AND STEWS'),
        ('not specified', 'NOT SPECIFIED'),
    )
    name = models.CharField(max_length=255, choices= CATEGORIES)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class RecipeModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="category")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipe_images/', default='recipe.svg', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class InstructionModel(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='instructions')
    step_number = models.PositiveIntegerField()
    instruction_text = models.TextField(null=True)

    class Meta:
        ordering = ['step_number']

class IngrediantsModel(models.Model):
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='ingrediants')
    name = models.CharField(max_length=100)