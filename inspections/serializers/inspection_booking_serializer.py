from rest_framework import serializers

from inspections.models import InspectionBooking


class InspectionBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionBooking
        fields = "__all__"
        read_only_fields = (
            "user",
            "status",
            "created_at",
        )