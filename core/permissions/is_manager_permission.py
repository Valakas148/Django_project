from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsManagerPermission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_manager and request.user.is_staff)

