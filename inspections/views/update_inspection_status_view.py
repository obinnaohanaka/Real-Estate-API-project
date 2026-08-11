from rest_framework import status, serializers
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from inspections.models import InspectionBooking


class InspectionStatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(
        choices=[
            "PENDING",
            "APPROVED",
            "REJECTED",
            "COMPLETED",
        ]
    )


class UpdateInspectionStatusView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = InspectionBooking.objects.all()
    serializer_class = InspectionStatusUpdateSerializer

    def patch(self, request, pk):
        try:
            booking = InspectionBooking.objects.get(pk=pk)
        except InspectionBooking.DoesNotExist:
            return Response(
                {"detail": "Inspection booking not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Only the listing owner (agent) can update the booking
        if booking.listing.agent != request.user:
            return Response(
                {"detail": "You do not have permission."},
                status=status.HTTP_403_FORBIDDEN,
            )

        new_status = request.data.get("status")

        valid_statuses = [
            "PENDING",
            "APPROVED",
            "REJECTED",
            "COMPLETED",
        ]

        if new_status not in valid_statuses:
            return Response(
                {
                    "detail": (
                        "Status must be one of: "
                        "PENDING, APPROVED, REJECTED, COMPLETED."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        booking.status = new_status
        booking.save()

        return Response(
            {
                "message": "Inspection status updated successfully.",
                "status": booking.status,
            },
            status=status.HTTP_200_OK,
        )