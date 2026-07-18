from django.urls import path
from agents.views.approve_agent_view import ApproveAgentView
from agents.views.register_agent_view import RegisterAgentView
from agents.views.dashboard_view import AgentDashboardView

urlpatterns = [
    path(
        "register/",
        RegisterAgentView.as_view(),
        name="register-agent",
    ),

    path(
        "<int:pk>/approve/",
        ApproveAgentView.as_view(),
        name="approve-agent",
    ),

    path(
        "dashboard/",
        AgentDashboardView.as_view(),
        name="agent-dashboard",
    ),
]