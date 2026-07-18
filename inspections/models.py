from django.conf import settings
from django.db import models

from listings.models import Listing


class InspectionBooking(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"
        COMPLETED = "COMPLETED", "Completed"

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="inspection_bookings",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inspection_bookings",
    )

    inspection_date = models.DateField()

    inspection_time = models.TimeField()

    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return (
            f"{self.user.email} - "
            f"{self.listing.title} - "
            f"{self.status}"
        )