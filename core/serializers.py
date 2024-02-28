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


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    subcategory_obj = serializers.SerializerMethodField()
    brand_obj = serializers.SerializerMethodField()
    
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=models.ProductSubCategory.objects.all()
    )
    brand = serializers.PrimaryKeyRelatedField(
        queryset=models.Brand.objects.all()
    )    
        
    def get_subcategory_obj(self, obj):
        if obj.subcategory:
            return {
                "name": obj.subcategory.name,
                "description": obj.subcategory.description
            }
    
    def get_brand_obj(self, obj):
        if obj.brand:
            return {
                "name": obj.brand.name
            }
    
    
    class Meta:
        model = models.Product
        fields = '__all__'
    