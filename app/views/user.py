from rest_framework import status
from rest_framework.response import Response
from app.serializers.user import UserCreateSerializer
from rest_framework.generics import CreateAPIView


class CreateAccount(CreateAPIView):
    serializer_class = UserCreateSerializer
