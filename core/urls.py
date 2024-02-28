from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register(r'product_categories', viewsets.ProductCategoryViewSet)
router.register(r'product_sub_categories', viewsets.ProductSubCategoryViewSet)
router.register(r'brand', viewsets.BrandViewSet)
router.register(r'products', viewsets.ProductViewSet)

urlpatterns = router.urls
