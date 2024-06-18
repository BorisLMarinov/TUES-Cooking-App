from django.db import models
from users.models import User

# Create your models here.
class Recipies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    cooking_time = models.CharField(max_length=100)
    cooking_instructions = models.TextField()

    def __str__(self):
        return self.recipe_name
