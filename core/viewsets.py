from rest_framework import viewsets, generics
from core import serializers
from core import models
from rest_framework import permissions
from core import filters
from core.pagination import BasePagination

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser,]
    pagination_class = BasePagination
    

class ProductSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.ProductSubCategory.objects.all()
    serializer_class = serializers.ProductSubCategorySerializer
    permission_classes = [permissions.IsAdminUser,]
    pagination_class = BasePagination


class BrandViewSet(viewsets.ModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [permissions.IsAdminUser,]
    pagination_class = BasePagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    permission_classes = [permissions.IsAdminUser,]
    pagination_class = BasePagination


class ProductShowCaseViewSet(generics.ListAPIView, viewsets.GenericViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    permission_classes = [permissions.AllowAny,]
    pagination_class = BasePagination

    def get_queryset(self):
        self.queryset = models.Product.objects.filter(
            availability=models.Product.Availability.AVAILABLE
        )

        return super().get_queryset()
