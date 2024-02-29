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
    category = serializers.CharField(source='subcategory.parent_category.name')
    subcategory = serializers.CharField(source='subcategory.name')
    brand = serializers.CharField(source='brand.name')
    category_id = serializers.CharField(source='subcategory.parent_category.id')
    brand_id = serializers.PrimaryKeyRelatedField(queryset=models.Brand.objects.all())    
    subcategory_id = serializers.PrimaryKeyRelatedField(
        queryset=models.ProductSubCategory.objects.all()
    )

    class Meta:
        model = models.Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order_item_price = serializers.FloatField(read_only=True)

    class Meta:
        model = models.OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Order
        fields = '__all__'
    