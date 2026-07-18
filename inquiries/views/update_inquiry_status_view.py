from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from inquiries.models import Inquiry


class UpdateInquiryStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, inquiry_id):
        try:
            inquiry = Inquiry.objects.get(id=inquiry_id)
        except Inquiry.DoesNotExist:
            return Response(
                {"detail": "Inquiry not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Only the listing owner can update the inquiry
        if inquiry.listing.agent != request.user:
            return Response(
                {
                    "detail": (
                        "You can only update inquiries "
                        "for your own listings."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        status_value = request.data.get("status")

        valid_statuses = [
            "PENDING",
            "RESPONDED",
            "CLOSED",
        ]

        if status_value not in valid_statuses:
            return Response(
                {"detail": "Invalid status."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        inquiry.status = status_value
        inquiry.save()

        return Response(
            {
                "detail": "Inquiry status updated successfully.",
                "status": inquiry.status,
            }
        )