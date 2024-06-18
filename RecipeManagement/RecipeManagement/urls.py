"""
URL configuration for RecipeManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from recipies import views as recipies_views
from users import views as users_views
from django.views.generic import ListView, DetailView, DeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recipies/", recipies_views.Recipe, name="recipies"),
    path("home/", recipies_views.Home, name="home"),
    path("", users_views.loginPage, name="login"),
    path("register/", users_views.signUp, name="register"),
    path("logout/", users_views.logoutPage, name="logout"),
    path("profile/<str:pk>", users_views.userProfile, name="profile"),
    path("add-recipe/", recipies_views.createRecipe, name="add-recipe"),
    path("edit-recipe/<int:pk>/", recipies_views.editRecipe, name="edit-recipe"),
    path("delete-recipe/<str:pk>/", recipies_views.deleteRecipe, name="delete-recipe"),
    path("edit-profile", users_views.editProfile, name="edit-profile"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
