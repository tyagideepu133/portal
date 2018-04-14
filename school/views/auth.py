from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..Serializers.auth import CustomUserLoginSerializer
from rest_framework import status, permissions


class UserLoginAPIView(APIView):
    """
    docstring here
        :param APIView: 
    """
    serializer_class = CustomUserLoginSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)