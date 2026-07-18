from django.urls import path

from property_images.views.upload_property_image_view import (
    UploadPropertyImageView,
)

urlpatterns = [
    path(
        "<int:listing_id>/upload/",
        UploadPropertyImageView.as_view(),
        name="upload-property-image",
    ),
]