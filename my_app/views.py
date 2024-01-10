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
            recipe = Recipe.objects.get(id=pk)
            a=RecipeSerializer(recipe).data
            return views.Response(a, status=status.HTTP_200_OK)
        except Recipe.DoesNotExist:
            return views.Response(status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        try:
            recipe_dict = request.POST
            recipe_serializer = RecipeSerializer(data=recipe_dict)
            if recipe_serializer.is_valid():
                recipe_serializer.save()
                return views.Response(recipe_serializer.data, status=status.HTTP_200_OK)
            else:
                return views.Response(status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return views.Response(status=status.HTTP_409_CONFLICT)


    def put(self, request, pk):
        try:
            instance = Recipe.objects.get(id=pk)
            recipe_serializer = RecipeSerializer(instance, data=request.data, partial=True)
            if recipe_serializer.is_valid():
                recipe_serializer.save()
                return views.Response(recipe_serializer.data, status=status.HTTP_200_OK)
            else:
                return views.Response(recipe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Recipe.DoesNotExist:
            return views.Response(status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk):
        try:
            recipe = Recipe.objects.get(id=pk)
            recipe.delete()
            return views.Response(status=status.HTTP_200_OK)
        except Recipe.DoesNotExist:
            return views.Response(status=status.HTTP_404_NOT_FOUND)


class RecipesView(views.APIView):
    """
    get list of recipes
    4 recipe receive
    """

    def get(self, request):
        return views.Response(Recipe.objects.values(), status=status.HTTP_200_OK)
