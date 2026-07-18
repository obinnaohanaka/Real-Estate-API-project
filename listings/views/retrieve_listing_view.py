from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny

from listings.models import Listing
from listings.serializers.listing_serializer import ListingSerializer


class RetrieveListingView(RetrieveAPIView):
    queryset = Listing.objects.filter(is_available=True)
    serializer_class = ListingSerializer
    permission_classes = [AllowAny]