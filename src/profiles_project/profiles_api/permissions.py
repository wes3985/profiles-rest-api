from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit theri own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id  # this checks that the object's id is the same as the user id
