from rest_framework import serializers

from web.core.models import Event, ProductCategory, Product


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'guest', 'description', 'date', 'time', 'image_url')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description')


class IdAndNameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name')

# -------------------------------------------------------------


class ProductSerializer(serializers.ModelSerializer):
    category = IdAndNameCategorySerializer

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'image_url', 'category')


