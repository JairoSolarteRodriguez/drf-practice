from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ allow the user edit own profile """

    def has_object_permissions(self, request, view, obj):
        """ check if the user tries to modify his own profile """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id