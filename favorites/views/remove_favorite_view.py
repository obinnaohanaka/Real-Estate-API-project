from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from favorites.models import Favorite


class RemoveFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, listing_id):
        try:
            favorite = Favorite.objects.get(
                user=request.user,
                listing_id=listing_id,
            )
        except Favorite.DoesNotExist:
            return Response(
                {"detail": "Favorite not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        favorite.delete()

        return Response(
            {"detail": "Favorite removed successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )