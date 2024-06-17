from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipies
from django.contrib.auth.decorators import login_required
from users.forms import User
from .forms import RecipeForm


# Create your views here.
@login_required(login_url="login")
def Home(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        return render(request, "recipies/home.html")


@login_required(login_url="login")
def Recipies(request):
    recipies = Recipies.objects.filter(user=request.user)
    return render(request, "recipies/recipies.html", {"recipies": recipies})


@login_required(login_url="login")
def createRecipe(request):
    form = RecipeForm
    if request.method == "POST":
        Recipies.objects.create(
            user=request.user,
            recipe_name=request.POST.get("recipe_name"),
            ingredients=request.POST.get("ingredients"),
            cooking_time=request.POST.get("cooking_time"),
            cooking_instructions=request.POST.get("cooking_instructions"),
        )
        return redirect("recipies")

    return render(request, "recipies/addrecipe.html", {"form": form})


@login_required(login_url="login")
def editRecipe(request, pk):
    recipies = Recipies.objects.get(id=pk)
    if request.user != recipies.user:
        return HttpResponse("You are not allowed here!")

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipies)
        if form.is_valid():
            form.save()
            return redirect("recipies")
    else:
        form = RecipeForm(instance=recipies)

    return render(request, "recipies/editrecipie.html", {"form": form})


@login_required(login_url="login")
def deleteRecipe(request, pk):

    recipies = Recipies.objects.get(id=pk)
    if request.user != recipies.user:
        return HttpResponse("You are not allowed here!")

    if request.method == "POST":
        recipies.delete()
        return redirect("recipies")

    return render(request, "recipies/deleterecipe.html", {"recipies": recipies})
