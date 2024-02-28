from rest_framework import viewsets
from account import models
from account import serializers
from account import permissions
# criar enpoint para criar usuario com endereço
# criar endpoint para mudar de senha
# criar enpoint esqueceu senha
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.UserPermissions,]

    def get_queryset(self):
        is_admin: bool = self.request.user.is_superuser \
            or self.request.user.is_staff
        
        if is_admin: 
            self.queryset = models.User.objects.all()
            return super().get_queryset()
        
        self.queryset = models.User.objects.filter(id=self.request.user.id)
        return super().get_queryset()
         

class UserAdressViewSet(viewsets.ModelViewSet):
    queryset = models.UserAdress.objects.all()
    serializer_class = serializers.UserAdress
    permission_classes = [permissions.UserAdressPermissions,]
    
    def get_queryset(self):
        is_admin: bool = self.request.user.is_superuser \
            or self.request.user.is_staff
        
        if is_admin: 
            self.queryset = models.UserAdress.objects.all()
            return super().get_queryset()
        
        self.queryset = models.UserAdress.objects.filter(user=self.request.user.id)
        return super().get_queryset()
    

        

