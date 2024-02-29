from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register(r'product_categories', viewsets.ProductCategoryViewSet)
router.register(r'product_sub_categories', viewsets.ProductSubCategoryViewSet)
router.register(r'brand', viewsets.BrandViewSet)
router.register(r'products', viewsets.ProductViewSet)
router.register(r'products_showcase', viewsets.ProductShowCaseViewSet, basename='product_showcase')
router.register(r'order_items', viewsets.OrderItemViewSet)
router.register(r'orders', viewsets.OrderViewSet)

urlpatterns = router.urls
