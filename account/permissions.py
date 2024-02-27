from ast import List
from rest_framework import permissions
from account import models
from account import managers

# endpoint: account/users/
# - Everyone can create a regular user account
# - Only authenticated users or admins can list
# - Only object owner or admin can Update or Delete
class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        is_admin: bool = \
            request.user.is_superuser or request.user.is_staff
        
        update_methods: List[str] \
            = request.method in ['PUT', 'PATCH', 'DELETE']

        if request.method == 'POST':
            return True

        if request.method == 'GET':
            return request.user.is_authenticated
        
        if update_methods and request.user.is_authenticated:
           return request.user.id == int(view.kwargs['pk']) or is_admin
        
        return False
    
# endpoint: account/adresses/
# - Only authencated users can create adresses
# - Only authenticated users or admins can list
# - Only object owner or admin can Update or Delete       
class UserAdressPermissions(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        is_admin: bool = \
            request.user.is_superuser or request.user.is_staff
        
        update_methods: List[str] \
            = request.method in ['PUT', 'PATCH', 'DELETE']

        if request.method == 'POST' or request.method == 'GET':
            return request.user.is_authenticated 
  
        if update_methods and request.user.is_authenticated:
            adress_owner = models.UserAdress.objects.is_adress_owner(
                user_id = request.user.id,
                target_adress_id = view.kwargs['pk']
            )

            return adress_owner or is_admin
           
        
        
        
        

