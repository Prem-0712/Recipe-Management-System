from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import RecipeModel, InstructionModel, IngrediantsModel, CategoryModel
from .forms import RecipeForm, InstructionForm, IngrediantsForm

@login_required
def view_user_recipes(request):
    recipes = RecipeModel.objects.filter(created_by = request.user)
    return render(request, 'recipe/view_user_recipes.html', {'recipes': recipes})

@login_required
def view_recipes(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = CategoryModel.objects.all()
    recipes = RecipeModel.objects.all()

    if category_id:
        recipes = recipes.filter(category_id= category_id)

    if query:
        recipes = recipes.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'recipe/view_recipes.html', {'recipes': recipes, 'categories': categories,})

@login_required
def view_recipe_detail(request, id_of_recipe):
    recipe = get_object_or_404(RecipeModel, pk = id_of_recipe)
    ingrediants = IngrediantsModel.objects.filter(recipe_id = id_of_recipe)
    instructions = InstructionModel.objects.filter(recipe_id = id_of_recipe)
    return render(request, 'recipe/view_recipe_detail.html', {'recipe': recipe, 'ing': ingrediants, 'ins': instructions})

@login_required
def create_recipe(request): 

    if (request.method == 'POST'): 
        form = RecipeForm(request.POST, request.FILES)

        if(form.is_valid()):
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            messages.success(request, 'Recipe created successfully..')
        
        else:
            messages.error(request, 'Failed to create recipe')
    
    else: 
        form = RecipeForm()
        

    return render(request, 'recipe/forms.html', {'form': form})

@login_required
def update_recipe(request, id):
    recipe = get_object_or_404(RecipeModel, pk = id, created_by = request.user)

    if (request.method == 'POST'): 
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Recipe updated successfully..')

        else:
            messages.error(request, 'Failed to update the recipe')

    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipe/forms.html', {'form': form})

@login_required
def delete_recipe(request, id):
    recipe = get_object_or_404(RecipeModel, pk = id, created_by = request.user)
    recipe.delete()
    messages.success(request, 'The recipe is deleted successfully...!!')
    return redirect('home')

@login_required
def create_ingrediants(request, id_of_recipe): 

    if (request.method == 'POST'):
        form = IngrediantsForm(request.POST)
        
        if (form.is_valid()):
            ingrediant = form.save(commit=False)
            ingrediant.recipe_id = id_of_recipe
            ingrediant.save()
            messages.success(request, 'Ingrediants created succesflly...')

        else:
            messages.error(request, 'Failed to make the ingrediants...')

    else:
        form = IngrediantsForm()

    return render(request, 'recipe/forms.html', {'form': form})

@login_required
def update_ingrediants(request, id, id_of_recipe):
    recipe = get_object_or_404( RecipeModel, pk = id_of_recipe, created_by = request.user)
    ingrediants = get_object_or_404(IngrediantsModel, pk = id, recipe = recipe)
    if (request.method == 'POST'): 
        form = IngrediantsForm(request.POST, instance= ingrediants)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Ingrediants updated succesfully...')

        else:
            messages.error(request, 'Failed to update ingrediants')
    else:
        form = IngrediantsForm(instance=ingrediants)

    return render(request, 'recipe/forms.html', {'form': form})

from django.shortcuts import redirect

@login_required
def delete_ingrediants(request, id, id_of_recipe):
    recipe = get_object_or_404(RecipeModel, pk=id_of_recipe, created_by=request.user)
    ingrediant = get_object_or_404(IngrediantsModel, pk=id, recipe=recipe)
    ingrediant.delete()
    messages.success(request, 'Ingrediant deleted successfully..')
    return redirect('recipe:view_recipe_detail', id_of_recipe=id_of_recipe)

@login_required
def create_instructions(request, id_of_recipe):
    recipe = get_object_or_404(RecipeModel, pk=id_of_recipe, created_by=request.user)
    
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            instruction = form.save(commit=False)
            instruction.recipe = recipe
            instruction.save()
            messages.success(request, 'Instructions created successfully...')
            return redirect('recipe:create_instruction', id_of_recipe=recipe.pk) 
        else:
            messages.error(request, 'Failed to create instructions...')
    else:
        form = InstructionForm()

    return render(request, 'recipe/forms.html', {'form': form})

@login_required
def update_instructions(request, id, id_of_recipe):

    recipe = get_object_or_404(RecipeModel, pk=id_of_recipe, created_by=request.user)
    instruction = get_object_or_404(InstructionModel, pk=id, recipe=recipe)

    if request.method == 'POST':
        form = InstructionForm(request.POST, instance=instruction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Instruction updated successfully.')
        else:
            messages.error(request, 'Failed to update instruction.')
    else:
        form = InstructionForm(instance=instruction)

    return render(request, 'recipe/forms.html', {'form': form})


@login_required
def delete_instructions(request, id, id_of_recipe):
    recipe = get_object_or_404(RecipeModel, pk=id_of_recipe, created_by=request.user)
    instruction = get_object_or_404(InstructionModel, pk=id, recipe=recipe)

    instruction.delete()
    messages.success(request, 'Instruction deleted successfully.')
    return redirect('recipe:view_recipe_detail', id_of_recipe=id_of_recipe)