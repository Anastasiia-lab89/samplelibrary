from rest_framework import permissions


class HasEditPermission(permissions.BasePermission):
    """
    Права на редактирование комментария.
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST' and request.user == obj.user:
            return True
        elif request.method == 'GET':
            return True
