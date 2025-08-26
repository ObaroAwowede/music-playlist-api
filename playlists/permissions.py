from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """This permission allows only owners to edit or delete objects, Everyone else is read only"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, 'owner',None) == request.user