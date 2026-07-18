from django.urls import path

from reviews.views.add_review_view import AddReviewView
from reviews.views.list_reviews_view import ListReviewsView
from reviews.views.update_review_view import UpdateReviewView
from reviews.views.delete_review_view import DeleteReviewView

urlpatterns = [
    path(
        "<int:listing_id>/add/",
        AddReviewView.as_view(),
        name="add-review",
    ),

    path(
        "<int:listing_id>/",
        ListReviewsView.as_view(),
        name="list-reviews",
    ),

    path(
        "<int:review_id>/update/",
        UpdateReviewView.as_view(),
        name="update-review",
    ),

    path(
        "<int:review_id>/delete/",
        DeleteReviewView.as_view(),
        name="delete-review",
    ),
]