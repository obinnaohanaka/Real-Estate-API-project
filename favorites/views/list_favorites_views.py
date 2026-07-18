from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from favorites.models import Favorite
from favorites.serializers.favorite_serializer import FavoriteSerializer


class ListFavoritesView(ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)