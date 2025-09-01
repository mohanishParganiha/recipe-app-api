"""
Views for the user API.
"""

from rest_framework import generics  # noqa
from user.serializers import UserSerializer  # noqa


class CreateUserView(generics.CreateAPIView):
    """create a new user in the system."""
    serializer_class = UserSerializer
