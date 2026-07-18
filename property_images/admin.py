from django.contrib import admin

from property_images.models import PropertyImage


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "listing",
        "uploaded_at",
    )