from rest_framework import serializers
from core import models

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = '__all__'
        

class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductSubCategory
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
    