from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from agents.models import AgentProfile
from listings.serializers.listing_serializer import ListingSerializer


class CreateListingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            agent_profile = AgentProfile.objects.get(user=request.user)
        except AgentProfile.DoesNotExist:
            return Response(
                {
                    "detail": "You must register as an agent first."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        if not agent_profile.is_approved:
            return Response(
                {
                    "detail": "Your agent account has not been approved."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ListingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(agent=request.user)

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )