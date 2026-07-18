from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers.reset_password_serializer import (
    ResetPasswordSerializer,
)


class ResetPasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user

            if not user.check_password(
                serializer.validated_data["old_password"]
            ):
                return Response(
                    {"detail": "Old password is incorrect."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(
                serializer.validated_data["new_password"]
            )

            user.save()

            return Response(
                {"detail": "Password updated successfully."},
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )