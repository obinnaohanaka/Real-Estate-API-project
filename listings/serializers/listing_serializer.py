from rest_framework import serializers

from listings.models import Listing


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = "__all__"
        read_only_fields = (
            "agent",
            "created_at",
            "updated_at",
        )