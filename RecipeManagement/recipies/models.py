from django.db import models
from users.models import User


# Create your models here.
class Recipies(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    cooking_time = models.IntegerField()
    cooking_instructions = models.TextField()
    user = models.ForeignKey(User, models.CASCADE)
    
    def __str__(self):
        return self.recipe_name
