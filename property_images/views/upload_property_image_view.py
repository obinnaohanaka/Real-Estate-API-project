from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from listings.models import Listing
from property_images.models import PropertyImage
from property_images.serializers.property_image_serializer import (
    PropertyImageSerializer,
)


class UploadPropertyImageView(CreateAPIView):
    serializer_class = PropertyImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, listing_id):
        try:
            listing = Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            return Response(
                {"detail": "Listing not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Only the owner of the listing can upload images
        if listing.agent != request.user:
            return Response(
                {"detail": "You can only upload images for your own listings."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(listing=listing)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)