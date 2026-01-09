from django.urls import path, include
from recipe import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('recipe', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
