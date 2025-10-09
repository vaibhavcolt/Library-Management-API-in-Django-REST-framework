from rest_framework import permissions
from rest_framework.permissions import BasePermission


class RoleAccessPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'
     
    def has_permission(self, request, view):
        return (
        request.user.is_authenticated and
        request.user.userrole_set.filter(role__name__in=['librarian']).exists()
        )