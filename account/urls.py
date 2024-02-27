


from rest_framework.routers import DefaultRouter
from account import viewsets

router = DefaultRouter()

router.register(r'users', viewsets.UserViewSet, basename='users')
router.register(r'user_adresses', viewsets.UserAdressViewSet, basename='user_adresses')

urlpatterns = router.urls