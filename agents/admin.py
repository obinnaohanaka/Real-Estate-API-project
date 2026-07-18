from django.contrib import admin
from .models import AgentProfile


@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "agency_name",
        "license_number",
        "is_approved",
        "created_at",
    )

    list_filter = (
        "is_approved",
        "created_at",
    )

    search_fields = (
        "user__email",
        "agency_name",
        "license_number",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )