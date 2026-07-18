from django.urls import path

from listings.views.create_listing_view import CreateListingView
from listings.views.list_listing_view import ListListingView
from listings.views.retrieve_listing_view import RetrieveListingView
from listings.views.update_listing_view import UpdateListingView
from listings.views.delete_listing_view import DeleteListingView

urlpatterns = [
    path(
        "",
        ListListingView.as_view(),
        name="list-listings",
    ),

    path(
        "create/",
        CreateListingView.as_view(),
        name="create-listing",
    ),

    path(
        "<int:pk>/update/",
        UpdateListingView.as_view(),
        name="update-listing",
    ),

    path(
        "<int:pk>/delete/",
        DeleteListingView.as_view(),
        name="delete-listing",
    ),

    path(
        "<int:pk>/",
        RetrieveListingView.as_view(),
        name="retrieve-listing",
    ),
]