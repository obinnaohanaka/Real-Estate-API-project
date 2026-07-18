from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from inspections.models import InspectionBooking
from inspections.serializers.inspection_booking_serializer import (
    InspectionBookingSerializer,
)


class ListInspectionBookingView(ListAPIView):
    serializer_class = InspectionBookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return InspectionBooking.objects.filter(
            user=self.request.user
        )