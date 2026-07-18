from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from listings.models import Listing
from listings.serializers.listing_serializer import ListingSerializer


class UpdateListingView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
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
                    "detail": "You can only update your own listings."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ListingSerializer(
            listing,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )