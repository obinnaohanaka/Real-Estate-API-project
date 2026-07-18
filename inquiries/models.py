from django.conf import settings
from django.db import models

from listings.models import Listing


class Inquiry(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("RESPONDED", "Responded"),
        ("CLOSED", "Closed"),
    ]

    listing = models.ForeignKey(
        Listing,
        on_delete=models.CASCADE,
        related_name="inquiries",
    )

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_inquiries",
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.email} -> {self.listing.title}"