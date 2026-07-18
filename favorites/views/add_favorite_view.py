from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from favorites.models import Favorite
from favorites.serializers.favorite_serializer import FavoriteSerializer
from listings.models import Listing


class AddFavoriteView(CreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, listing_id):
        try:
            listing = Listing.objects.get(id=listing_id)
        except Listing.DoesNotExist:
            return Response(
                {"detail": "Listing not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        favorite, created = Favorite.objects.get_or_create(
            user=request.user,
            listing=listing,
        )

        if not created:
            return Response(
                {"detail": "Listing already in favorites."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(favorite)
        return Response(serializer.data, status=status.HTTP_201_CREATED)