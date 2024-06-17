from django.forms import ModelForm
from .models import Recipies
from users.models import User

class RecipeForm(ModelForm):
    class Meta:
        model = Recipies
        fields = ["recipe_name", "ingredients", "cooking_time", "cooking_instructions"]


class EditRecipeForm(ModelForm):
    class Meta:
        model = Recipies
        fields = ["recipe_name", "ingredients", "cooking_time", "cooking_instructions"]
        