from rest_framework import  IsAdminUser, SAFE_METHOD



class IsAdminOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):

        if request.method in SAFE_METHOD:
            return True
        return bool(request.user and request.user.is_staff)