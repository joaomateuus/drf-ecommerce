from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()

router.register(r'product_categories', viewsets.ProductCategoryViewSet)
router.register(r'products', viewsets.ProductViewSet)

urlpatterns = router.urls
