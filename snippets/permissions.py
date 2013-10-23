from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  """
  Customer permission to only allow owners of an object to edit import
  """

  def has_object_permission(self, request, view, obj):
    #read per are allowed to any request
    if request.method in permissions.SAFE_METHODS:
      return True

    #write permission are only allow to the owner

    return obj.owner == request.user

