from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from agents.serializers.register_agent_serializer import (
    RegisterAgentSerializer,
)


class RegisterAgentView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=RegisterAgentSerializer,
        responses={
            201: "Agent application submitted successfully.",
            400: "Invalid data.",
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