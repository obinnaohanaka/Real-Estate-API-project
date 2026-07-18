from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from reviews.models import Review
from reviews.serializers.review_serializer import ReviewSerializer


class ListReviewsView(ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        listing_id = self.kwargs["listing_id"]
        return Review.objects.filter(listing_id=listing_id)