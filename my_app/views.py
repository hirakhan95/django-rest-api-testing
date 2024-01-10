from rest_framework import views, status

from .models import Recipe
from .serializer import RecipeSerializer


# Create your views here.

class SingleRecipeView(views.APIView):
    """
    get single recipe api
    it should have title, author name, methods, ingredients
    """

    def get(self, request, pk):
        try:
            res = RecipeSerializer(Recipe.objects.get(id=pk)).data
        except Recipe.DoesNotExist:
            return views.Response(status=status.HTTP_404_NOT_FOUND)
        return views.Response(res, status=status.HTTP_200_OK)

    def post(self, request):
        recipe = RecipeSerializer(data=request.POST)
        if recipe.is_valid():
            recipe.save()
            return views.Response(status=status.HTTP_200_OK)
        else:
            return views.Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            recipe = Recipe.objects.get(id=pk)
        except Recipe.DoesNotExist:
            return views.Response(status=status.HTTP_404_NOT_FOUND)

        recipe_serializer = RecipeSerializer(recipe, data=request.POST, partial=True)

        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return views.Response(status=status.HTTP_200_OK)
        else:
            return views.Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(id=pk)
        except Recipe.DoesNotExist:
            return views.Response(status=status.HTTP_404_NOT_FOUND)
        recipe.delete()
        return views.Response(status=status.HTTP_200_OK)


class RecipesView(views.APIView):
    """
    get list of recipes
    4 recipe receive
    """

    def get(self, request):
        return views.Response(Recipe.objects.values(), status=status.HTTP_200_OK)