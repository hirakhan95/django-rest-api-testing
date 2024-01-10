from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=30)
    title = serializers.CharField(max_length=30)
    ingredients = serializers.CharField(max_length=500)
    method = serializers.CharField(max_length=500)

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.ingredients = validated_data.get('ingredients', instance.ingredients)
        instance.method = validated_data.get('method', instance.method)
        instance.save()
        return instance

    class Meta:
        model = Recipe
