from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from accounts.serializers.register_serializer import RegisterSerializer


class RegisterView(APIView):
    """
    Register a new user.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(
            {"message": "User registered successfully."},
            status=status.HTTP_201_CREATED,
        )