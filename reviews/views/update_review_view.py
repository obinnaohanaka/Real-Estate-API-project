from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from reviews.models import Review


class UpdateReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, review_id):
        try:
            review = Review.objects.get(
                id=review_id,
                user=request.user,
            )
        except Review.DoesNotExist:
            return Response(
                {"detail": "Review not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        review.rating = request.data.get(
            "rating",
            review.rating,
        )

        review.comment = request.data.get(
            "comment",
            review.comment,
        )

        review.save()

        return Response(
            {
                "detail": "Review updated successfully."
            }
        )