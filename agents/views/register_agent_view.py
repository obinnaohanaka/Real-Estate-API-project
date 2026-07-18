from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from agents.serializers.register_agent_serializer import (
    RegisterAgentSerializer,
)


class RegisterAgentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RegisterAgentSerializer(
            data=request.data,
            context={"request": request},
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Agent application submitted successfully.",
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )