from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from agents.serializers.register_agent_serializer import (
    RegisterAgentSerializer,
)


class RegisterAgentView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=RegisterAgentSerializer,
        responses={
            201: {
                "description": "Agent application submitted successfully."
            }
        },
    )
    def post(self, request):
        serializer = RegisterAgentSerializer(
            data=request.data,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Agent application submitted successfully.",
            },
            status=status.HTTP_201_CREATED,
        )