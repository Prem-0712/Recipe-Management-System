from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.view_recipes, name='view_recipes'),
    path('view_user_recipes/', views.view_user_recipes, name='view_user_recipes'),
    path('view_recipe_detail/<int:id_of_recipe>/', views.view_recipe_detail, name='view_recipe_detail'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:id>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:id>/', views.delete_recipe, name='delete_recipe'),
    path('<int:id_of_recipe>/create_ingrediants/', views.create_ingrediants, name='create_ingrediants'),
    path('<int:id_of_recipe>/update_ingrediants/<int:id>/', views.update_ingrediants, name='update_ingrediants'),
    path('<int:id_of_recipe>/delete_ingrediants/<int:id>/', views.delete_ingrediants, name='delete_ingrediants'),
    path('<int:id_of_recipe>/create_instruction/', views.create_instructions, name='create_instruction'),
    path('<int:id_of_recipe>/update_instruction/<int:id>/', views.update_instructions, name='update_instruction'),
    path('<int:id_of_recipe>/delete_instructions/<int:id>/', views.delete_instructions, name='delete_instructions'),
]
