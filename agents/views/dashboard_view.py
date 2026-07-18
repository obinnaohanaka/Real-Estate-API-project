from django.db.models import Avg, Count
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from listings.models import Listing


class AgentDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        listings = Listing.objects.filter(agent=request.user)

        total_listings = listings.count()

        available_listings = listings.filter(
            is_available=True
        ).count()

        unavailable_listings = listings.filter(
            is_available=False
        ).count()

        total_favorites = 0
        total_inquiries = 0

        for listing in listings:
            total_favorites += listing.favorited_by.count()
            total_inquiries += listing.inquiries.count()

        average_rating = (
            listings.aggregate(
                average=Avg("reviews__rating")
            )["average"]
            or 0
        )

        return Response(
            {
                "total_listings": total_listings,
                "available_listings": available_listings,
                "unavailable_listings": unavailable_listings,
                "total_favorites": total_favorites,
                "total_inquiries": total_inquiries,
                "average_rating": round(
                    average_rating,
                    2,
                ),
            }
        )