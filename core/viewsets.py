from rest_framework import viewsets, generics
from rest_framework.decorators import action
from core import serializers
from core import models
from rest_framework import permissions
from core import filters
from core.pagination import BasePagination
from rest_framework.response import Response
from core import request_validator
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


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated,]

# criar sinal para fazer update do valor do order item refletir no order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.IsAuthenticated,]

    @action(detail=False, methods=['POST'], serializer_class=request_validator.CreateOrderItemSerializer)
    def create_order_item(self, request, *args, **kwargs):
        try:
            rv = request_validator.CreateOrderItemSerializer(data=request.data)
            rv.is_valid(raise_exception=True)

            order_use_case = use_cases.OrderUseCase(**rv.validated_data)
            order = order_use_case.main()
            serializer = serializers.OrderSerializer(order)

            return Response(data=serializer.data, status=200)
        except Exception as e:
            print(str(e))
            return Response(data='Was not posible to create an item order', status=400)