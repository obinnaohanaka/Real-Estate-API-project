from django.urls import path

from favorites.views.add_favorite_view import AddFavoriteView
from favorites.views.list_favorites_views import ListFavoritesView
from favorites.views.remove_favorite_view import RemoveFavoriteView

urlpatterns = [
    path(
        "<int:listing_id>/add/",
        AddFavoriteView.as_view(),
        name="add-favorite",
    ),

    path(
        "",
        ListFavoritesView.as_view(),
        name="list-favorites",
    ),

    path(
        "<int:listing_id>/remove/",
        RemoveFavoriteView.as_view(),
        name="remove-favorite",
    ),
]