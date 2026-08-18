from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User


class DeleteUserView(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Prevent an admin from accidentally deleting themselves
        if user == request.user:
            return Response(
                {"detail": "You cannot delete your own account."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.delete()

        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )