from django import forms
from .models import RecipeModel, InstructionModel, IngrediantsModel

SELECT_AREA = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

INPUT_AREA = 'rounded-none rounded-e-lg bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'

TEXT_AREA = 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = ['category', 'name', 'image', 'description']
        widgets = {
            'category': forms.Select(attrs={'class': SELECT_AREA}),
            'name': forms.TextInput(attrs={'class': INPUT_AREA, 'placeholder': 'Recipe Name'}),
            'image': forms.FileInput(attrs={'class': FOR_IMAGE}),
            'description': forms.Textarea(attrs={'class': TEXT_AREA, 'placeholder': 'Enter description here', 'rows': 3}),
        }

class InstructionForm(forms.ModelForm):
    class Meta:
        model = InstructionModel
        fields = ['step_number', 'instruction_text']
        widgets = {
            'step_number': forms.NumberInput(attrs={'class': INPUT_AREA}),
            'instruction_text': forms.Textarea(attrs={'class': TEXT_AREA, 'placeholder': 'Enter instruction'}),
        }

class IngrediantsForm(forms.ModelForm):
    class Meta:
        model = IngrediantsModel
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_AREA, 'placeholder': 'Ingredient name'}),
        }