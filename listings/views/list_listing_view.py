from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from listings.models import Listing
from listings.serializers.listing_serializer import ListingSerializer


class ListListingView(ListAPIView):
    queryset = Listing.objects.filter(is_available=True)
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]

    search_fields = [
        "title",
        "description",
        "city",
        "state",
    ]
    
    
    filterset_fields = [
        "city",
        "state",
        "listing_type",
        "property_type",
        "bedrooms",
        "bathrooms",
        "is_available",
    ]

    ordering_fields = [
        "price",
        "created_at",
        "bedrooms",
        "bathrooms",
    ]

    ordering = ["-created_at"]