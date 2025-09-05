"""
Views for the user API.
"""

from rest_framework import generics  # noqa
from rest_framework.authtoken.views import ObtainAuthToken  # noqa
from rest_framework.settings import api_settings    # noqa
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
    )  # noqa


class CreateUserView(generics.CreateAPIView):
    """create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
