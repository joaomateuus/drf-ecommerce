from rest_framework import viewsets
from core import serializers
from core import models
from rest_framework import permissions
from core import filters

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser,]
    

class ProductSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductSubCategory.objects.all()
    serializer_class = serializers.ProductSubCategorySerializer
    permission_classes = [permissions.IsAdminUser,]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [permissions.IsAdminUser,]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    permission_classes = [permissions.IsAdminUser,]
