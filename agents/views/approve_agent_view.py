from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from agents.models import AgentProfile


class ApproveAgentView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        agent = get_object_or_404(
            AgentProfile,
            pk=pk,
        )

        if request.user.role != "ADMIN":
            return Response(
                {
                    "detail": "Only admins can approve agents."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        agent.is_approved = True
        agent.approved_by = request.user
        agent.approved_at = timezone.now()

        agent.save()

        return Response(
            {
                "message": "Agent approved successfully."
            },
            status=status.HTTP_200_OK,
        )