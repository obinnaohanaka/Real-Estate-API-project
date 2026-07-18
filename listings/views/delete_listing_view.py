from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from listings.models import Listing


class DeleteListingView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            listing = Listing.objects.get(pk=pk)
        except Listing.DoesNotExist:
            return Response(
                {"detail": "Listing not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if listing.agent != request.user:
            return Response(
                {
                    "detail": "You can only delete your own listings."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        listing.delete()

        return Response(
            {
                "message": "Listing deleted successfully."
            },
            status=status.HTTP_204_NO_CONTENT,
        )