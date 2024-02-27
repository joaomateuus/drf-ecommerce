from rest_framework import viewsets
from account import models
from account import serializers
from rest_framework.permissions import AllowAny
from account import permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

# criar enpoint para criar usuario com endereço
# criar endpoint para mudar de senha
# criar enpoint esqueceu senha
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.UserPermissions,]

    def get_queryset(self):
        is_admin: bool \
            = self.request.user.is_superuser or self.request.user.is_staff
        
        if is_admin:
            return models.User.objects.all()
        
        return models.User.objects.filter(id=self.request.user.id)
         

class UserAdressViewSet(viewsets.ModelViewSet):
    queryset = models.UserAdress.objects.all()
    serializer_class = serializers.UserAdress
    permission_classes = [TokenHasReadWriteScope, permissions.UserAdressPermissions]
    
    def get_queryset(self):
        is_admin: bool = \
            self.request.user.is_superuser or self.request.user.is_staff
        
        if is_admin:
            return models.UserAdress.objects.all()
        
        return models.UserAdress.objects.filter(user=self.request.user.id)

