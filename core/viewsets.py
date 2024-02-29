from rest_framework import viewsets, generics
from rest_framework.decorators import action
from core import serializers
from core import models
from rest_framework import permissions
from core import filters
from core.pagination import BasePagination
from rest_framework.response import Response
from core import use_cases

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
    queryset = models.Product.objects.filter(
        availability=models.Product.Availability.AVAILABLE
    )
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    permission_classes = [permissions.AllowAny,]
    pagination_class = BasePagination
    
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated,]
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)

            order_use_case = use_cases.OrderUseCase(
                user=serializer.validated_data['user'],
                product=serializer.validated_data['product'],
                quantity=serializer.validated_data['quantity']
            )
            order = order_use_case.main()
            order_serializer = serializers.OrderSerializer(order)

            return Response(data=order_serializer.data, status=200)
        except Exception as e:
            print(str(e))
            return Response(data='Was not posible to create an item order', status=400)
        
        
class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated,]