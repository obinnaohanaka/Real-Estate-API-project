from django.contrib import admin

from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "agent",
        "price",
        "listing_type",
        "category",
        "city",
        "is_available",
        "created_at",
    )

    list_filter = (
        "listing_type",
        "category",
        "city",
        "is_available",
    )

    search_fields = (
        "title",
        "city",
        "state",
        "agent__email",
    )