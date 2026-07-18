from django.conf import settings
from django.db import models


class AgentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="agent_profile",
    )

    agency_name = models.CharField(max_length=255)

    license_number = models.CharField(
        max_length=100,
        unique=True,
    )

    years_of_experience = models.PositiveIntegerField(default=0)

    bio = models.TextField(blank=True)

    is_approved = models.BooleanField(default=False)

    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_agents",
    )

    approved_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.user.email} - {self.agency_name}"