from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets

from api.v1.serializers.user_serializer import UserSerializer


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    '''Users viewset.'''

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'head', 'options', 'post', 'patch', 'delete']
    permission_classes = (permissions.IsAdminUser,)