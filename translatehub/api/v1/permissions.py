from rest_framework.response import Response
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.status import HTTP_200_OK, HTTP_402_PAYMENT_REQUIRED, HTTP_409_CONFLICT


class IsAuthorOrIsAdmin(BasePermission):
    ...


